#include <iostream>

using namespace std;

class Maze {
  public:
    Maze();
};

class Wall {
  public:
    Wall();
};

class Room {
  public:
    Room(int n);
};

class Door {
  public:
    Door(Room* r1, Room* r2);
};

class MazeFactory {
  public:
    MazeFactory();

    virtual Maze* MakeMaze() const {
      return new Maze;
    }
    virtual Wall* MakeWall() const {
      return new Wall;
    }
    virtual Room* MakeRoom(int n) const {
      return new Room(n);
    }
    virtual Door* MakeDoor(Room* r1, Room* r2) const {
      return new Door(r1, r2);
    }
};

int main() {
  cout << "Success\n";
  return 0;
}
