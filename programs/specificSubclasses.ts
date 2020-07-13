class Employee {
  constructor(public name: string) {  
  }
}

class Manager extends Employee {
}

class Executive extends Employee {
}

// department accept only subclass of employees
class Department<T extends Employee> {
   //different types of employees
   private employees:Array<T> = new Array<T>();
   public add(employee: T): void {
      this.employees.push(employee);
  }
  public display(): void {
    console.log(this.employees);
   }
}

let m: Department<Manager> = new Department();
m.add(new Manager("arung"));
m.add(new Manager("vijay"));
m.display();
let e: Department<Executive> = new Department();
e.add(new Executive("asish"));
e.add(new Executive("madhu"));
e.display();
