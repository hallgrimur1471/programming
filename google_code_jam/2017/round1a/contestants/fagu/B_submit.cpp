#line 1 "B.cpp"
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <string>
#include <cassert>
#include <cmath>
#include <cstring>
#include <functional>
#include <random>
using namespace std;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef long long ll;
#define REP(i,a,n) for (int i = (a); i < (n); i++)

template<class T> T& setmin(T &a, const T &b) {return a = min(a, b);}
template<class T> T& setmax(T &a, const T &b) {return a = max(a, b);}
template<class T> T MODD(const T &a, const T &b) {T r = a%b; if (r < 0) r += b; return r;}




///////////////////////////////// BEGIN util.h /////////////////////////////////


#line 1 "util.h"
template <class T, class U>
ostream& operator<<(ostream &o, const pair<T,U> &p) {
	return o << "(" << p.first << ", " << p.second << ")";
}

template <class T>
ostream& print_list(ostream &o, const T &v) {
	o << "[";
	bool first = true;
	for (const auto &t : v) {
		if (first)
			first = false;
		else
			o << ", ";
		o << t;
	}
	return o << "]";
}

template <class T>
ostream& print_map(ostream &o, const T &v) {
	o << "{";
	bool first = true;
	for (const auto &t : v) {
		if (first)
			first = false;
		else
			o << ", ";
		o << t.first << " => " << t.second;
	}
	return o << "}";
}

template <class T>
ostream& operator<<(ostream &o, const vector<T> &v) {
	return print_list(o, v);
}

template <class T>
ostream& operator<<(ostream &o, const set<T> &v) {
	return print_list(o, v);
}

template <class T,size_t N>
ostream& operator<<(ostream &o, const array<T,N> &v) {
	return print_list(o, v);
}

template <class T,class U>
ostream& operator<<(ostream &o, const map<T,U> &v) {
	return print_map(o, v);
}

template <class T, size_t N>
struct TuplePrintHelper {
	static ostream& print(ostream& o, const T &t) {
		TuplePrintHelper<T,N-1>::print(o, t);
		o << ", ";
		return o << get<N-1>(t);
	}
};

template <class T>
struct TuplePrintHelper<T,1> {
	static ostream& print(ostream& o, const T &t) {
		return o << get<0>(t);
	}
};

template <class T>
struct TuplePrintHelper<T,0> {
	static ostream& print(ostream& o, const T &) {
		return o;
	}
};

template <class... Args>
ostream& operator<<(ostream &o, const tuple<Args...> &t) {
	o << "(";
	TuplePrintHelper<tuple<Args...>, sizeof...(Args)>::print(o, t);
	return o << ")";
}


template <class T>
T fastpow(const T &a, ll n) {
	T r = 1, e = a;
	for (int i = 0; (1ll<<i) <= n; i++, e *= e) {
		if (n&(1ll<<i))
			r *= e;
	}
	return r;
}



///////////////////////////////// END util.h /////////////////////////////////


#line 30 "B.cpp"

int testcasenr;

int N, P;
int R[100];
int Q[100][100];
int p[100];

void docase() {
	scanf("%d%d", &N, &P);
	REP(n,0,N)
		scanf("%d", R+n);
	REP(n,0,N) {
		REP(p,0,P)
			scanf("%d", &Q[n][p]);
		sort(Q[n], Q[n]+P);
	}
	REP(n,0,N)
		p[n] = 0;
	int res = 0;
	for (int s = 1; ;) {
		bool bad = false;
		bool good = true;
		REP(n,0,N) {
			while(p[n] < P && 100ll*Q[n][p[n]] < 90ll*R[n]*s)
				p[n]++;
			if (p[n] == P)
				bad = true;
			else if (100ll*Q[n][p[n]] > 110ll*R[n]*s)
				good = false;
		}
		if (bad)
			break;
		if (good) {
			res++;
			REP(n,0,N)
				p[n]++;
		} else {
			s++;
		}
	}
	printf("%d\n", res);
}

int main() {
	int T;
	scanf("%d ", &T);
	for (testcasenr = 1; testcasenr <= T; testcasenr++) {
		fprintf(stderr, "Test %d/%d\n", testcasenr, T);
		printf("Case #%d: ", testcasenr);
		docase();
		fflush(stdout);
		fflush(stderr);
	}
	return 0;
}
