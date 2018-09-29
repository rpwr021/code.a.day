From a given line, find out how many vowels each word has then create a pair of words each word having its unique set of vowels (no repeats)

#### Part 1 
  *  Write a function that will take a sentence and count the number of letters in each word which are vowels (a, e, i, o, u, y).
  * 
  * Example:
  * Input: "the quick brown fox jumps over the lazy dog"
  * Expected result: Array[(String, Int)] = Array((the,1), (quick,2), (brown,1), (fox,1), (jumps,1), (over,2), (the,1), (lazy,2), (dog,1))


#### Part 2 
  *  Now write a function that will take these word counts as input and output the top K pairs of words that together have the most *unique* vowels.
  *    It should skip mirrored pairs and self-pairs, and have no duplicates.
  * 
  * Example for K=3:  Seq((over,quick,4), (lazy,quick,4), (lazy,over,4))


