class Solution:
    import itertools
    def letterCombinations(self, digits: str) -> List[str]:
        import itertools
        number_dict = {
                        1:[""],
                        2 : ['a','b','c'],
                        3 : ['d','e','f'], 
                        4 : ['g','h','i'], 
                        5 : ['j','k','l'],
                        6 : ['m','n','o'],
                        7 : ['p','q','r','s'],
                        8 : ['t','u','v'],
                        9 : ['w','x','y','z'],
        }
        digits = [number_dict[int(i)] for i in digits]
        if [""] in digits:
            digits.remove([""])
        output = list(itertools.product(*digits))
        for j in range(len(output)):
            output[j] = "".join(output[j])
        if output == [""]:
            output = []

        return(output)