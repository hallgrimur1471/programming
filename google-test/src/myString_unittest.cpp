#include "myString.h"
#include "gtest/gtest.h"
namespace {

// Tests the default constructor
TEST(MyString, DefaultConstructor) {
  const MyString s;

  // Assers that s.c_string() returns NULL
  EXPECT_STREQ(NULL, s.c_string());
  EXPECT_EQ(0u, s.Length());
}

const char kHelloString[] = "Hello, world!";

// Tests the constructor that accepts a C string.
TEST(MyString, constructorFromCString) {
  const MyString s(kHelloString);
  EXPECT_EQ(0, strcmp(s.c_string(), kHelloString));
  EXPECT_EQ(sizeof(kHelloString)/sizeof(kHelloString[0]) -1, s.Length());
}

// Tests the Set method.
TEST(MyString, Set) {
  MyString s;

  s.Set(kHelloString);
  EXPECT_EQ(0, strcmp(s.c_string(), kHelloString));

  // Set should work when the input pointer is the same as the one
  // already in the MyString object.
  s.Set(s.c_string());
  EXPECT_EQ(0, strcmp(s.c_string(), kHelloString));

  // Can we set the MyString to NULL?
  s.Set(NULL);
  EXPECT_STREQ(NULL, s.c_string());
}
}  // namespace
