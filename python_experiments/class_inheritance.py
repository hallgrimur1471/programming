#!/usr/bin/env python3

class A:
    def launch(self):
        #
        # a lot of crazy lines
        # doing crazy stuff
        print("Tear the roof off the sucker")
        self.launch2()

    def launch2(self):
        self._funk()
    
    def _funk(self):
        print("We want the funk")

class B(A):
    def launch(self):
        #
        # do something new here
        #

        #
        # now we want to run all the "crazy lines" in A.launch
        # but when self.funk() is called we want to run B.funk
        # how do you do that?
        super().launch()

    def _funk(self):
        print("Give up the funk")

b = B()
b.launch()

# desired output:
#     Tear the roof off the sucker
#     Give up the funk
