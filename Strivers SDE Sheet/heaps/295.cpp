#include <queue>
using namespace std;

class MedianFinder {
public:
    priority_queue<int> left;
    priority_queue<int, vector<int>, greater<int>> right;

    MedianFinder() {}

    void addNum(int num) {
        left.push(num);
        right.push(left.top());
        left.pop();

        if (left.size() < right.size()) {
            left.push(right.top());
            right.pop();
        }
    }
    double findMedian() {
        if (left.size() > right.size()) {
            return left.top();
        } else {
            return (left.top() + right.top()) / 2.0;
        }
    }
};
