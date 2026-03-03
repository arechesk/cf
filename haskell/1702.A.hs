import Control.Monad (replicateM_)

main :: IO ()
main = do
    t <- readLn  -- read number of test cases
    replicateM_ t $ do
        s <- getLine                     -- read number as string
        let n = read s :: Integer         -- convert to Integer
            p = 10 ^ (length s - 1)       -- 10^(len-1)
        print (n - p)                     -- output result
