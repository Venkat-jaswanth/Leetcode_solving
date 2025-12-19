#include <iostream>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace __gnu_pbds;
using namespace std;
template<typename T> 
using ordered_set = tree<
    T,
    null_type,
    less<T>,
    rb_tree_tag,
    tree_order_statistics_node_update
>;


//s.insert(x);
//s.erase(x);
//s.find_by_order(k);   // iterator
//s.order_of_key(x);    // count < x

//Fast insert/delete
//Fast “k-th element” queries
//finding the k-th smallest element and counting elements less than a given value, all in \(O(\log n)\) time

int main() {
    ordered_set<int> s;
    s.insert(2);
    s.insert(9);
    s.insert(3);

    // Count elements strictly less than 9
    cout << s.order_of_key(9) << endl; // Outputs 2 (elements 2, 3)

    // Find the 1st smallest element (0-based index)
    cout << *(s.find_by_order(1)) << endl; // Outputs 3

    return 0;
}

