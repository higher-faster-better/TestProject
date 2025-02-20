#include <string>
#include <cassert>
#include <sstream>
#include <cctype>
#include <iostream>

std::string reverse_word(const std::string &word) {
    std::string reversed;
    for (int i = word.size() - 1; i >= 0; --i) {
        reversed += word[i];
    }
    return reversed;
}

std::string reverse_words(const std::string &str) {
    std::ostringstream result;
    std::string word;
    
    for (size_t i = 0; i < str.size(); ++i) {
        if (std::isalnum(str[i])) {
            word += str[i];
        } else {
            if (!word.empty()) {
                result << reverse_word(word);
                word.clear();
            }
            result << str[i];
        }
    }

    if (!word.empty()) {
        result << reverse_word(word);
    }

    return result.str();
}

int main() {
    std::string test_str = "String; 2be reversed...";
    assert(reverse_words(test_str) == "gnirtS; eb2 desrever...");
    
    // Additional test cases
    assert(reverse_words("Hello, World!") == "olleH, dlroW!");
    assert(reverse_words("123 456!") == "321 654!");
    assert(reverse_words("A B C") == "A B C");

    std::cout << "All tests passed!" << std::endl;
    return 0;
}
