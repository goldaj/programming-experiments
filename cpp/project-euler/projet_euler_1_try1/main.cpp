#include <iostream>
#include <cmath>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int i, j = 0, k = 0, l = 0, n, t;
	int r = 0;
	int l_stop = 0;
	int k_stop = 0;

	cin >> t;
	vector<int> resultat(t);

    for(i = 0; i < t; i += 1) {
		cin >> n;
		while (j < n) {
			r = r + j + k + l;

			if(l_stop == 0) l += 15;
			if(l >= n) {l = 0; l_stop = 1;}

			if(k_stop == 0) {
				k += 5;
				if((k % 15) == 0) k += 5;
			}

			if(k >= n) {k = 0; k_stop = 1;}
			j += 3;
			if((j % 15) == 0) j += 3;
			if((j % 5) == 0) j += 3;
		}
		resultat[i] = r;
		j = 0; k = 0; l = 0;
		k_stop = 0; l_stop = 0;
		r = 0;
    }
    for(i = 0; i < t; i += 1) {
		cout << resultat[i] << endl;
    }
    return 0;
}
