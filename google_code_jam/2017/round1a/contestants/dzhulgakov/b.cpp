#define _CRT_SECURE_NO_WARNINGS
#include <algorithm>
#include <numeric>
#include <string>
#include <cstring>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <cassert>

using namespace std;

#define REP(i,n) for (int i=0,_n=(n); i < _n; i++)
#define REPD(i,n) for (int i=(n)-1; i >= 0; i--)
#define FOR(i,a,b) for (int _b=(b), i=(a); i <= _b; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))

#define CLEAR(x) memset(x,0,sizeof x);
#define CLEARA(x) memset(&x,0,sizeof x);
#define FILL(x,v) memset(x,v,sizeof x);
#define FILLA(x,v) memset(&x,v,sizeof x);

#define VAR(a,b) __typeof(b) a=(b)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)

#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 0x7fffffff
#define X first
#define Y second
#define pb push_back
#define SZ(c) (int)(c).size()
#define MP make_pair
#define eps 1.0e-11
const double pi = acos(-1.0);

typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long LL;

#define N 1024

int n,k;
int a[N][N];
int q[N];

LL dvup(LL x, LL y) { return (x+y-1)/y; }

int main(int argc, char **argv)
{
	string FN = "B-large";
	if (argc>1) FN = string(argv[1]);
	int shift = 0;
	if (argc>2) sscanf(argv[2],"%d",&shift);
	freopen((FN+".in").c_str(),"r",stdin);
	freopen((FN+".out").c_str(),"w",stdout);

	int tests;
	scanf("%d",&tests);
	for (int test = 1; test<=tests; test++)
	{
		fprintf(stderr,"=== %s : %d\n", FN.c_str(), test+shift);
		printf("Case #%d: ",test+shift);
		////////////////////////////////////////////////////////////
		scanf("%d%d",&n,&k);
		REP(i,n) scanf("%d", &q[i]);
		REP(i,n) REP(j,k) scanf("%d",&a[i][j]);
		REP(i,n) sort(a[i], a[i]+k);
		int ind[N];
		REP(i,n) ind[i]=0;
		int res=0;
		while (true) {
			bool end=false;
			REP(i,n) if (ind[i] >= k) end=true;
			if (end) break;
			LL lower=0,upper=1000000000;
			double mn = 1.0e20;
			int best =-1;
			REP(i,n) {
				LL up = 10LL * a[i][ind[i]] / (9LL * q[i]);
				LL lw = dvup(10LL * a[i][ind[i]], (11LL * q[i]));
				double dup = (10.0 * a[i][ind[i]]) / (9.0 * q[i]);
				double dlw = (10.0 * a[i][ind[i]]) / (11.0 * q[i]);
				lower=max(lower,lw);
				upper=min(upper,up);
				if (dlw < mn) { mn=dlw; best=i; }
			}
			if (lower <= upper) {
				++res;
				REP(i,n)++ind[i];
			}
			else
			{
				++ind[best];
			}
		}
		printf("%d\n",res);
	}
	fprintf(stderr,"=== %s DONE\n", FN.c_str());
	return 0;
}