#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

// Function to find two indices such that their sum equals the target
vector<int> twoSum(const vector<int>& nums, int target) {
    unordered_map<int, int> num_map; // Map to store the value and its index

    for (int i = 0; i < nums.size(); ++i) {
        int complement = target - nums[i];
        if (num_map.find(complement) != num_map.end()) {
            return {num_map[complement], i};
        }
        num_map[nums[i]] = i;
    }
    return {}; // Return an empty vector if no solution is found
}

// int main() {
//     // Define multiple test cases
//     vector<pair<vector<int>, int>> testCases = {
//         {{2, 7, 11, 15}, 9},
//         {{3, 2, 4}, 6},
//         {{3, 3}, 6},
//         {{1, 2, 3, 4, 5}, 10} // No solution case
//     };

//     // Iterate through each test case
//     for (const auto& [nums, target] : testCases) {
//         vector<int> result = twoSum(nums, target);
        
//         // Print the results
//         if (!result.empty()) {
//             cout << "Test case - Target: " << target << ", Indices: " << result[0] << ", " << result[1] << endl;
//         } else {
//             cout << "Test case - Target: " << target << ", No solution found" << endl;
//         }
//     }

//     return 0;
// }