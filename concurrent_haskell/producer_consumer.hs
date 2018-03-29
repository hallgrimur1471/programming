import Control.Concurrent

-- cvar is a name of a mutable location that is either empty or contains a value
--
-- producer will put 'x' into cvar, consumer will take it out.
-- cvar can only contain a single value at a time.
main = do
    cvar <- newCVar
    forkIO (producer cvar 'x')
    consumer cvar

-- MVar can almost be used to make this producer/consumer connection.
-- Where the producer puts values into the MVar and the consumer takes them out.
-- The problem is that there is nothing to stop the producer of putting
-- a value in the MVar when there is already a value there. This would produce
-- an error. This problem is easily solved, by using a second MVar (ack_var) 
-- which the producer will "ask" if there already is a value in the other MVar.
-- We encapsulate this functionality in a new data type, the CVar.

type CVar a = (MVar a,  -- producer -> consumer
               MVar ()) -- consumer -> producer

newCVar = do
    data_var <- newEmptyMVar
    ack_var  <- newEmptyMVar
    putMVar ack_var ()
    return (data_var, ack_var)

putCVar (data_var, ack_var) val = do
    takeMVar ack_var
    putStr "produced "
    putMVar data_var val

getCVar (data_var, ack_var) = do
    val <- takeMVar data_var
    putStr "consumed "
    putMVar ack_var ()
    return val

producer cvar val = do
    putCVar cvar val
    producer cvar val

consumer cvar = do
    getCVar cvar
    consumer cvar
