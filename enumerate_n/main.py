class Solution:
    def enumerate_n(self,n:int)->[int]:
        primes = []
        is_prime = [False,False]+[True]*(n-1)

        for p in range(2,n+1):
            if is_prime[p]:
                primes.append(p)
            # seive's future prime numbers
            for i in range(p*2,n+1,p):
                is_prime[i] = False
        return primes

if __name__== "__main__":
        mySolution = Solution()
        print(mySolution.enumerate_n(88))
