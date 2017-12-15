class Person

class Student extends Person

class Child1 extends Student

class Child2 extends Child1

class Pair[T](val first: T, val second: T) {
  // 设置下界，最后始终返回T的类型
  def replaceFirst[R >: T](newFirst: R) = {
//    println(newFirst.getClass)
//    println(second.getClass)
    new Pair(newFirst, second)
  }
  // 上界
  def replaceSecond[R <: T](newScond: R) = {
    new Pair(first, newScond)
  }
}


var p = new Person
var s = new Student()
var c = new Child1

var p1 = new Pair(p,p)
p1.replaceFirst(c)

var s1 = new Pair(s,s)
s1.replaceFirst(c)
s1.replaceFirst(p)
s1.replaceFirst(new Child2)


var c1 = new Pair(c,c)
c1.replaceFirst(s)
c1.replaceFirst(p)
c1.replaceFirst(new Child2)


// s
var r = new Pair(s, s)
r.replaceSecond(p)


