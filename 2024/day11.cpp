#include <iostream>
#include <stdexcept>
#include <fstream>
#include <sstream>
#include <vector>
#include <cmath>
#include <thread>
#include <mutex>
#include <functional>
#include <set>

int digits(int64_t x) {
    if (x >= 10000000000) {
        if (x >= 100000000000000) {
            if (x >= 10000000000000000) {
                if (x >= 100000000000000000) {
                    if (x >= 1000000000000000000)
                        return 19;
                    return 18;
                }
                return 17;
            }
            if (x >= 1000000000000000)
                return 16;
            return 15;
        } 
        if (x >= 1000000000000) {
            if (x >= 10000000000000)
                return 14;
            return 13;
        }
        if (x >= 100000000000)
            return 12;
        return 11;
    }
    if (x >= 100000) {
        if (x >= 10000000) {
            if (x >= 100000000) {
                if (x >= 1000000000)
                    return 10;
                return 9;
            }
            return 8;
        }
        if (x >= 1000000)
            return 7;
        return 6;
    }
    if (x >= 100) {
        if (x >= 1000) {
            if (x >= 10000)
                return 5;
            return 4;
        }
        return 3;
    }
    if (x >= 10)
        return 2;
    return 1;
}

// Function to process a chunk of numbers
void processChunk(const std::vector<int64_t> chunk, std::vector<int64_t>& results, std::mutex& resultMutex) {
    std::vector<int64_t> localResults; // Local storage to minimize locking
    for (const auto& stone : chunk) {
        int intLength = digits(stone);
        if (stone == 0) {
            localResults.push_back(1);
        } else if (intLength % 2 == 0) {
            int halfLen = intLength / 2;
            localResults.push_back(stone / static_cast<int64_t>(std::pow(10, halfLen)));
            localResults.push_back(stone % static_cast<int64_t>(std::pow(10, halfLen)));
        } else {
            localResults.push_back(stone * 2024);
        }
    }
    // Lock and append to the shared results vector
    std::lock_guard<std::mutex> lock(resultMutex);
    results.insert(results.end(), localResults.begin(), localResults.end());
}

void parallelProcessing(std::vector<int64_t>& numbers, int numThreads) {
    std::vector<int64_t> nextBlink;
    std::mutex resultMutex;

    // Determine chunk size
    size_t chunkSize = (numbers.size() + numThreads - 1) / numThreads;
    // Create and launch threads
    std::vector<std::thread> threads;
    for (int i = 0; i < numThreads; ++i) {
        size_t startIdx = i * chunkSize;
        size_t endIdx = std::min(startIdx + chunkSize, numbers.size());
        if (startIdx >= endIdx) break; // No more data to process

        std::vector<int64_t> chunk(numbers.begin() + startIdx, numbers.begin() + endIdx);
        threads.emplace_back(processChunk, chunk, std::ref(nextBlink), std::ref(resultMutex));
    }

    // Join threads
    for (auto& t : threads) {
        t.join();
    }

    numbers = std::move(nextBlink);
}

int main() {
    int64_t star1 = 0;
    int64_t star2 = 0;
    int64_t blinks = 75;
    std::ifstream file("day11.txt");
    if (!file.is_open()) {
        std::cerr << "Could not open the file!" << std::endl;
        return 1;
    }

    std::vector<int64_t> numbers;
    std::string line;
    
    while (std::getline(file, line)) {
        std::istringstream stream(line);
        int64_t number;
        while (stream >> number) {
            numbers.push_back(number);
        }
    }
    file.close();

    // numbers = {125, 17};

    int numThreads = 64; // Adjust the number of threads as needed

    for (int64_t blink = 1; blink < blinks + 1; blink++) {
        std::cout << "processing blink " << blink << std::endl;

        // Use parallel processing to compute the next state of `numbers`
        parallelProcessing(numbers, numThreads);

        if (blink == 25) {
            star1 = numbers.size();
            std::cout << "star1: " << star1 << std::endl;
        }


        std::set<int64_t> uniqueNumbers(numbers.begin(), numbers.end());
        // this is when i realized the correct solution, implemented in day11.py
        std::cout << "total elements: " << numbers.size() << std::endl;
        std::cout << "unique elements: " << uniqueNumbers.size() << std::endl;
        std::cout << "average duplicates: " << (numbers.size()/uniqueNumbers.size()) << std::endl;
    }
    
    star2 = numbers.size();
    std::cout << "star2: " << star2 << std::endl;

    return 0;
}