#include <iostream>

enum Direction{North, South, East, West};

class MapSite {
 public:
  virtual void Enter() = 0;
};

class Room : public MapSite {
 public:
  explicit Room(int roomNo) {}

  MapSite* GetSide(Direction) const;
  void SetSide(Direction, MapSite*) {}

  virtual void Enter() {}

 private:
  MapSite* _sides[4];
  int _roomNumber;
};

class Wall : public MapSite {
 public:
  Wall() {}
  virtual void Enter() {}
};

class Door : public MapSite {
 public:
  explicit Door(Room* = 0, Room* = 0) {}

  virtual void Enter() {}
  Room* OtherSideFrom(Room*);

 private:
  Room* _room1;
  Room* _room2;
  bool _isOpen;
};

class Maze {
 public:
  Maze() {}
  void AddRoom(Room*) {}
  Room* RoomNo(int) const;
};

// Abstract factory
class MazeFactory {
 public:
  MazeFactory() {}

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

class MazeGame {
 public:
  Maze* CreateMaze();
  Maze* CreateMaze(MazeFactory& factory);
};

// Straight forward implementation of CreateMaze:

Maze* MazeGame::CreateMaze() {
  Maze* aMaze = new Maze;
  Room* r1 = new Room(1);
  Room* r2 = new Room(2);
  Door* theDoor = new Door(r1, r2);

  aMaze->AddRoom(r1);
  aMaze->AddRoom(r2);

  r1->SetSide(North, new Wall);
  r1->SetSide(East, theDoor);
  r1->SetSide(South, new Wall);
  r1->SetSide(West, new Wall);

  r2->SetSide(North, new Wall);
  r2->SetSide(East, new Wall);
  r2->SetSide(South, new Wall);
  r2->SetSide(West, theDoor);

  return aMaze;
}

// We can use the Abstract factory in CreateMaze implementation to avoid
// hard-coding used classes.

Maze* MazeGame::CreateMaze(MazeFactory& factory) {
  Maze* aMaze = factory.MakeMaze();
  Room* r1 = factory.MakeRoom(1);
  Room* r2 = factory.MakeRoom(2);
  Door* theDoor = factory.MakeDoor(r1, r2);

  aMaze->AddRoom(r1);
  aMaze->AddRoom(r2);

  r1->SetSide(North, new Wall);
  r1->SetSide(East, theDoor);
  r1->SetSide(South, new Wall);
  r1->SetSide(West, new Wall);

  r2->SetSide(North, new Wall);
  r2->SetSide(East, new Wall);
  r2->SetSide(South, new Wall);
  r2->SetSide(West, theDoor);

  return aMaze;
}

// Example: EnchantedMazeFactory

class Spell {
  Spell();
};

class EnchantedRoom : public Room {
 public:
  EnchantedRoom(int n, Spell* spell);
};

class DoorNeedingSpell : public Door {
 public:
  DoorNeedingSpell(Room* r1, Room* r2);
};

class EnchantedMazeFactory : public MazeFactory {
 public:
  EnchantedMazeFactory();

  virtual Room* MakeRoom(int n) const {
    return new EnchantedRoom(n, CastSpell());
  }

  virtual Door* MakeDoor(Room* r1, Room* r2) const {
    return new DoorNeedingSpell(r1, r2);
  }

 protected:
  Spell* CastSpell() const;
};

// Example: BombedMazeFactory

class BombedWall : public Wall {
 public:
  BombedWall() {}
};

class RoomWithABomb : public Room {
 public:
  explicit RoomWithABomb(int n) : Room(n) {}
};

class BombedMazeFactory : public MazeFactory {
 public:
  BombedMazeFactory() {}

  Wall* MakeWall() const {
    return new BombedWall;
  }

  Room* MakeRoom(int n) const {
    return new RoomWithABomb(n);
  }
};

int main() {
  MazeGame game1;
  BombedMazeFactory factory1;
  game1.CreateMaze(factory1);

  MazeGame game2;
  EnchantedMazeFactory factory2;
  game2.CreateMaze(factory2)

  std::cout << "Success\n";
  return 0;
}
