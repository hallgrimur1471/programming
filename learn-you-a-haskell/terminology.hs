-- *** IMPORTS ***
-- Writer Monad:
--     Control.Monad.Writer

-- *** TERMINOLOGY ***
-- x data type
-- x type constructor
-- x value constructor
-- x type
-- record syntax
-- type synonym
-- record syntax
-- constructor
-- typeclass
-- functor
-- applicative functor
-- monoid
-- monad

-- *************************************************
-- data type, type constructor, type parameter, type
-- *************************************************
-- in the example
data Maybe a = Nothing | Just a
-- Maybe         is a   type constructor
-- a (left one)  is a   type parameter
-- a (right one) is a   type parameter
-- Maybe a       is a   data type
-- Maybe Int     is a   type
-- Just          is a   value constructor
-- Just a         is a   value constructor that has 1 field
data Bool = False | True
-- Bool          is a   data type
-- Bool          is a   type
-- False         is a   value constructor
-- False         is a   value
-- True          is a   value constructor
-- True          is a   value
data Person = Person String Int
-- String              is a   type
-- Int                 is a   type
-- Person String Int   is a   value constructor that has 2 field types
-- "hi"                is a   value
-- Person "hi" 18      is a   value

-- *****************
-- value constructor
-- *****************
-- see "data type"

-- type synonym:
type Birds = Int
type Pole = (Birds,Birds)

-- type class
--     type can be an instance of a type class

-- functors
--     for things that can be mapped over

-- monoid
--     implements "mappend" ('pure"?)
