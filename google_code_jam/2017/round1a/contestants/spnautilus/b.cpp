// spnauT
//
#include <bits/stdc++.h>
using namespace std;
#define FOR(i,a,b) for(int _b=(b),i=(a);i<_b;++i)
#define ROF(i,b,a) for(int _a=(a),i=(b);i>_a;--i)
#define REP(n) for(int _n=(n);_n--;)
#define _1 first
#define _2 second
#define PB(x) push_back(x)
#define SZ(x) int((x).size())
#define ALL(x) (x).begin(),(x).end()
#define MSET(m,v) memset(m,v,sizeof(m))
#define MAX_PQ(T) priority_queue<T>
#define MIN_PQ(T) priority_queue<T,vector<T>,greater<T>>
#define IO(){ios_base::sync_with_stdio(0);cin.tie(0);}
#define nl '\n'
#define cint1(a) int a;cin>>a
#define cint2(a,b) int a,b;cin>>a>>b
#define cint3(a,b,c) int a,b,c;cin>>a>>b>>c
typedef long long LL;typedef pair<int,int> PII;
typedef vector<int>VI;typedef vector<LL>VL;typedef vector<PII>VP;
template<class A,class B>inline bool mina(A &x,const B &y){return(y<x)?(x=y,1):0;}
template<class A,class B>inline bool maxa(A &x,const B &y){return(x<y)?(x=y,1):0;}

#define MAXN (64)

int N, P;
int R[MAXN];
MIN_PQ(PII) Q[MAXN];

int main()
{
	cint1(TT);
	FOR(T,1,TT+1)
	{
		cin >> N >> P;
		FOR(i,0,N) cin >> R[i];

		FOR(i,0,N) REP(P)
		{
			cint1(a);
			int x = (10*a + 11*R[i] - 1) / (11*R[i]);
			int y = (10*a) / (9*R[i]);

			if(x <= y) Q[i].push(PII(x,y));
		}

		int sol = 0;
		while(1)
		{
			int x = 1;
			int y = 1e9;
			FOR(i,0,N)
			{
				if(Q[i].empty()) goto end;
				int xx, yy;
				tie(xx,yy) = Q[i].top();
				maxa(x,xx);
				mina(y,yy);
			}

			if(x <= y)
			{
				++sol;
				FOR(i,0,N) Q[i].pop();
			}
			else
			{
				FOR(i,0,N) if(Q[i].top()._2 == y) Q[i].pop();
			}
		}

end:
		printf("Case #%d: %d\n", T, sol);

		FOR(i,0,N) while(!Q[i].empty()) Q[i].pop();
	}

	return 0;
}