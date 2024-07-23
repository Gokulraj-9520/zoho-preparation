import time
class Employee:
    def __init__(self, emp_id, name, department, manager_id=None):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.manager_id = manager_id

class EmployeeManagementSystem:
    def __init__(self):
        self.employees = {}

    def add_employee(self, emp_id, name, department, manager_id=None):
        if emp_id in self.employees:
            print(f"Employee with ID {emp_id} already exists.")
            time.sleep(2)
            return
        self.employees[emp_id] = Employee(emp_id, name, department, manager_id)
        print(f"Employee {name} added successfully.")
        time.sleep(2)

    def update_employee(self, emp_id, name=None, department=None, manager_id=None):
        if emp_id not in self.employees:
            print(f"Employee with ID {emp_id} does not exist.")
            time.sleep(2)
            return
        if name:
            self.employees[emp_id].name = name
        if department:
            self.employees[emp_id].department = department
        if manager_id:
            self.employees[emp_id].manager_id = manager_id
        print(f"Employee {emp_id} updated successfully.")
        time.sleep(2)

    def delete_employee(self, emp_id):
        if emp_id not in self.employees:
            print(f"Employee with ID {emp_id} does not exist.")
            time.sleep(2)
            return
        del self.employees[emp_id]
        print(f"Employee {emp_id} deleted successfully.")
        time.sleep(2)

    def search_employee(self, name=None, department=None):
        results = []
        for emp in self.employees.values():
            if (name and name in emp.name) or (department and department == emp.department):
                results.append(emp)
        return results

    def display_hierarchy(self, emp_id, level=0):
        if emp_id not in self.employees:
            print(f"Employee with ID {emp_id} does not exist.")
            time.sleep(2)
            return
        print("  " * level + f"{self.employees[emp_id].name} ({self.employees[emp_id].emp_id})")
        
        for sub_id in self.employees:
            if self.employees[sub_id].manager_id == emp_id:
                self.display_hierarchy(sub_id, level + 1)
        time.sleep(2)
    def check_circular_reference(self):
        visited = set()
        def visit(emp_id):
            if emp_id in visited:
                return False
            visited.add(emp_id)
            manager_id = self.employees[emp_id].manager_id
            if manager_id and manager_id in self.employees:
                return visit(manager_id)
            return True

        for emp_id in self.employees:
            visited.clear()
            if not visit(emp_id):
                return False
        return True

def main():
    system = EmployeeManagementSystem()

    while True:
        print("\n1. Add Employee")
        print("2. Update Employee")
        print("3. Delete Employee")
        print("4. Search Employee")
        print("5. Display Hierarchy")
        print("6. Check Circular Reference")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            department = input("Enter Department: ")
            manager_id = input("Enter Manager ID (optional): ") or None
            system.add_employee(emp_id, name, department, manager_id)

        elif choice == '2':
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Name (optional): ") or None
            department = input("Enter Department (optional): ") or None
            manager_id = input("Enter Manager ID (optional): ") or None
            system.update_employee(emp_id, name, department, manager_id)

        elif choice == '3':
            emp_id = input("Enter Employee ID: ")
            system.delete_employee(emp_id)

        elif choice == '4':
            name = input("Enter Name to search (optional): ") or None
            department = input("Enter Department to search (optional): ") or None
            results = system.search_employee(name, department)
            for emp in results:
                print(f"{emp.name} ({emp.emp_id}) - {emp.department}")

        elif choice == '5':
            emp_id = input("Enter Employee ID to display hierarchy: ")
            system.display_hierarchy(emp_id)

        elif choice == '6':
            if system.check_circular_reference():
                print("No circular references found.")
            else:
                print("Circular references detected!")

        elif choice == '7':
            print("Thanks You, You are welcome !..")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
