using System;



Solution1 solution = new Solution1();
int[] nums = { 2, 7, 11, 15 };
int target = 9;
int[] result = solution.TwoSum(nums, target);

if (result != null)
{
    Console.WriteLine($"My Solution: [{result[0]}, {result[1]}]");
}
else
{
    Console.WriteLine("No solution found.");
}