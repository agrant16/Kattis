//Goldbach's Conjecture

#include <iostream>
#include <vector>

using namespace std;

vector<int> primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29};

// dedup and getPrimes compose a Sieve algorithm for finding prime numbers
void dedup(vector<int>& v, int n, int p)
{
    for (int i = 0; i < v.size(); i++) 
    {
        if (v[i] != p && v[i] % p == 0)
            v.erase(v.begin() + i);
    }
}

void getPrimes(vector<int>& v, int n)
{
    int biggest = v[v.size() - 1];
    if (n > ( biggest + 1))
    {
        for (int i = biggest + 2; i < n; i += 2)
            v.push_back(i);

        int len = v.size();
        int x = 0;
    
        while (x < len)
        {
            dedup(v, n, v[x]);
            x++;
            len = v.size();         
        }
    }
}

void sums(vector<int> v, int n, vector<int>& ans) 
{
    for (int x : v)
    {
        int y = v.size() - 1;
        while(v[y] >= x && y > -1)
        {
            if (v[y] + x == n)
                ans.push_back(x);
            y--;
        }
    }
}

int main(int argc, char** argv)
{
    vector<int> ans;
    int cases;
    int n;
    cin >> cases;
    
    for (int i = 0; i < cases; i++)
    {
        cin >> n;

        getPrimes(primes, n);

        sums(primes, n, ans);

        cout << n << " has " << ans.size() << " representation(s)" << endl;

        for (int x : ans)
            cout << x << "+" << (n - x) << endl;

        ans.clear();
    }
}

