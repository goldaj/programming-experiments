#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
	int exp_day, exp_month, exp_year;
	int ret_day, ret_month, ret_year;

	cin >> ret_day; cin >> ret_month; cin >> ret_year;
	cin >> exp_day; cin >> exp_month; cin >> exp_year;

	if(ret_year > exp_year) cout << 10000;
    else if(exp_year > ret_year) cout << 0;
    else {
		if(ret_month > exp_month) cout << 500 * (ret_month - exp_month);
		else if(exp_month > ret_month) cout << 0;
		else {
			if (ret_day > exp_day) cout << 15 * (ret_day - exp_day);
			else cout << 0;
		}
    }

	return 0;
}
