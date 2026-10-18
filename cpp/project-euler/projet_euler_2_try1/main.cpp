#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <unordered_map>
using namespace std;

#define P 40000000000000000

int fib (long long n, long long* r)
{
    static std::unordered_map<int,int> cache;

    if (cache.find(n) == cache.end())
    {
        int f;
        if (n==0)
            f = 0;
        else if (n < 3)
            f = 1;
        else if (n % 2 == 0)
        {
            int k = n/2;
            f = (fib(k, r) * (2*fib(k+1, r) - fib(k, r))) % P;
        }
        else
        {
            int k = (n-1)/2;
            f = (fib(k+1, r)*fib(k+1, r)+ fib(k, r) * fib(k, r)) % P;
        }
        if (f<0)
            f += P;

        cache[n] = f;
    }
    if(f % 2 == 0) r += f;
    return cache.at(n);
}

int main ()
{
    long long i, t, n;
    long long* f = 0;

    cin >> t;
    for(i = 0; i < t; i += 1) {
		cin >> n;
		fib(n, f);
		cout << f << endl;
    }
	return 0;
}
