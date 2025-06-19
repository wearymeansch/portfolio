#include <bits/stdc++.h>

using namespace std;

using ll = long long;

#include <ext/pb_ds/assoc_container.hpp>

using namespace __gnu_pbds;

template <typename T>
using ordered_set = tree<T, null_type, less<T>, rb_tree_tag,
                         tree_order_statistics_node_update>;

int main() {
/*#ifdef GOLIKOV
  assert(freopen("in", "rt", stdin));
  auto _clock_start = chrono::high_resolution_clock::now();
#endif*/
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int n, k;
  cin >> n >> k;
  vector<int> a(n);
  for (auto& x : a) {
    cin >> x;
  }
  int const INF = int(1.1e9);
  multiset<int> vals;
  vector<int> b(n, INF);
  for (int i = 0; i < n; ++i) {
    vals.insert(a[i]);
    if (i >= k - 1) {
      b[i - (k - 1)] = *vals.rbegin();
      vals.erase(vals.find(a[i - (k - 1)]));
    }
  }
  for (auto x : b)
     cout<<x<<' ';
  cout<<endl;

  set<int> nonactiveB;
  vector<pair<int, int>> events;
  for (int i = 0; i < n; ++i) {
    nonactiveB.insert(i);
    events.emplace_back(a[i], i);
    events.emplace_back(b[i], ~i);
  }
  nonactiveB.insert(-1);
  nonactiveB.insert(n);
  sort(events.rbegin(), events.rend());
  ll ans = 0;

  auto getPrev = [&](int x) {
    return *prev(nonactiveB.upper_bound(x));/*upper_bound в set возвращает итератор, указывающий
#на первый элемент, который больше значения х, в питоне анaлогом является функция bisect_right.
#getPrev возвращает ссылку на значение x (или ближайшее, которое меньше его, при отсутствии x)
#в списке nonactiveB, возможна ошибка, если x меньше всех значений в nonactiveB*/
  };
  auto getNext = [&](int x) {
    return *nonactiveB.lower_bound(x);
  };
  ordered_set<int> activeA;
  auto getA = [&](int l, int r) {
    return int(activeA.order_of_key(r) - activeA.order_of_key(l));
  };

  for (auto[x, t] : events) {
     cout<<x<<' '<<t<<endl;
  }
  for (auto[x, t] : events) {
    if (t < 0) {
      t = ~t;
      assert(b[t] == x);
      nonactiveB.erase(t);
      int from = getPrev(t);
      int to = getNext(t);
      cout<<"b "<<t<<' '<<b[t]<<' '<<from<<' '<<to<<' '<<getA(from + 1, t + 1)<<' '<< activeA.order_of_key(from + 1)<<' '<< activeA.order_of_key(t + 1) <<' '<<getA(t, to)<<' '<< activeA.order_of_key(t)<<' ' << activeA.order_of_key(to);
      assert(from <= t);
      assert(to >= t);
      ans += ll(x) * getA(from + 1, t + 1) * getA(t, to);
    } else {
      assert(a[t] == x);
      activeA.insert(t);
      int from = getPrev(t);
      int to = getNext(t);
      cout<<"a "<<t<<' '<<a[t]<<' '<<from<<' '<<to;
      if (from + 1 <= to) {
        ans += ll(x) * getA(from + 1, to);
        cout<<' '<<getA(from + 1, to)<<' '<< activeA.order_of_key(from + 1)<<' '<< activeA.order_of_key(to);
      }
    }
    cout<<' '<<ans<<endl;
  }
  cout << ans << '\n';

#ifdef GOLIKOV
  cerr << "Executed in " << chrono::duration_cast<chrono::milliseconds>(
      chrono::high_resolution_clock::now()
          - _clock_start).count() << "ms." << endl;
#endif
  return 0;
}
