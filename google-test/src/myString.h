#include <string.h>

class MyString {
 private:
    const char* c_string_;
    const MyString& operator=(const MyString& rhs);

 public:
    // Clones a 0-terminated C string, allocating memory using new.
    static const char* CloneCString(const char* a_c_string);

    /////////////////////////////////////////////////////////////////
    // Constructors

    // The default constructor contstructs a NULL String.
    MyString() : c_string_(NULL) {}

    // Constructs a MyString by cloning a 0-terminated C string.
    explicit MyString(const char* a_c_string) : c_string_(NULL) {
      Set(a_c_string);
    }

    // End: Constructors
    /////////////////////////////////////////////////////////////////

    // Destructor. MyString is intended to be a final class, so the destructor
    // doesn't need to be virtual
    ~MyString() { delete[] c_string_; }

    // Gets the 0-terminated C string this MyString object represents.
    const char* c_string() const { return c_string_;  }

    size_t Length() const {
      return c_string_ == NULL ? 0 : strlen(c_string_);
    }

    // Sets the 0-terminated C string this MyString object represents.
    void Set(const char* a_c_string);
};
