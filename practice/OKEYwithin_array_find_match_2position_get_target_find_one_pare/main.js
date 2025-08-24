function twoSum(nums, target) {
    const seen = {};  // Use an object as a hash map

    for (let i = 0; i < nums.length; i++) {
        // console.log(i)
        // process.exit();
        const num = nums[i];
        const complement = target - num;

        if (seen.hasOwnProperty(complement)) {
            return [seen[complement], i];  // Return the stored index and current index
        }

        seen[num] = i;  // Store the current number and its index
    }

    return null;  // If no match is found
}


const nums = [5, 7, 3, 2];
const target = 9;

console.log(twoSum(nums, target));  // Output: [0, 3] → because 5 + 4 = 9
