import qualified Data.Map as Map

instance Functor (Map.Map k) where
    fmap f m = Map.map f m 
