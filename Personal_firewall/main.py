import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout, result.stderr

def view_rules():
	stdout, stderr = run_command("sudo iptables -L")
	if stderr:
		print("Error:", stderr)
	print(stdout)

def add_rule(chain, protocol, port, action):
    command = f"sudo iptables -A {chain} -p {protocol} --dport {port} -j {action}"
    stdout, stderr = run_command(command)
    if stderr:
        print("Error:", stderr)
    else:
        print("Rule added successfully.")

def remove_rule(chain, protocol, port, action):
    command = f"sudo iptables -D {chain} -p {protocol} --dport {port} -j {action}"
    stdout, stderr = run_command(command)
    if stderr:
        print("Error:", stderr)
    else:
        print("Rule removed successfully.")

def main():
    while True:
        print("1. View Rules")
        print("2. Add Rule")
        print("3. Remove Rule")
        print("4. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            view_rules()
        elif choice == "2":
            chain = input("Enter chain (INPUT, OUTPUT, FORWARD): ")
            protocol = input("Enter protocol (tcp, udp): ")
            port = input("Enter port: ")
            action = input("Enter action (ACCEPT, DROP, REJECT): ")
            add_rule(chain, protocol, port, action)
        elif choice == "3":
            chain = input("Enter chain (INPUT, OUTPUT, FORWARD): ")
            protocol = input("Enter protocol (tcp, udp): ")
            port = input("Enter port: ")
            action = input("Enter action (ACCEPT, DROP, REJECT): ")
            remove_rule(chain, protocol, port, action)
        elif choice == "4":
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()

