#include <iostream>
#include <climits>

using namespace std;

int greedyChange(int coinSet[], int coinSetSize, int pendingChange) {
  if (pendingChange == 0) {
    return 0;
  }
  if (pendingChange < 0) {
    return INT_MAX;
  }
  int coins = INT_MAX;
  for (int i = 0; i < coinSetSize; i++) {
    int result = greedyChange(coinSet, coinSetSize, pendingChange - coinSet[i]);
    if (result != INT_MAX) {
      coins = min(coins, result + 1);
    }
  }
  return coins;
};

int main(int argc, char const *argv[])
{
  int coinSet[] = {1, 5, 10, 15, 20};
  int coinSetSize = sizeof(coinSet)/sizeof(int);
  int change = 27;
  cout << "Minimal quantity of coins: " << greedyChange(coinSet, coinSetSize, change) << endl;
  return 0;
}