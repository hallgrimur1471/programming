// compile:
// p=boost_useage; g++ -I /usr/local/boost_1_67_0 -std=c++17 -o $p ${p}.cpp
//
// run:
// echo "1 2 3" | ./$p
//
#include <algorithm>
#include <boost/lambda/lambda.hpp>
#include <iostream>
#include <iterator>

int main() {
  using namespace boost::lambda;
  typedef std::istream_iterator<int> in;

  std::for_each(in(std::cin), in(), std::cout << (_1 * 3) << " ");
  std::cout << std::endl;
}
