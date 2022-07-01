// https://www.programminghunter.com/article/39761745659/

# include <bits/stdc++.h>

using namespace std;
typedef long long ll;
ll n, l, r, s = 1, ans;
void solve(ll a, ll b, ll l, ll r, ll d){//二分的思想
    if ( a > b || l > r )    return;
    else{
        ll mid = (a+b)/2;
        if ( r < mid )solve(a,mid-1,l,r,d/2);
        else if ( mid < l )solve(mid+1,b,l,r,d/2);
        else {
            ans += d%2;
            solve(a,mid-1,l,mid-1,d/2);
            solve(mid+1,b,mid+1,r,d/2);
        }
    }
}
int main(){
    cin >> n >> l >> r;
    ll p = n;
    while ( p >= 2 ){
        p /= 2;
        s = s*2+1;
    }
    solve(1,s,l,r,n);
    cout << ans << endl;
    return 0;
}