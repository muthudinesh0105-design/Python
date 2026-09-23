                print(f"Found! Time: {result.entry_time} | Visitor: {result.visitor_name}")
            else:
                print("Log entry not found.")
            display_logs(tree)
               
        elif choice == '4':
            print("\nChoose Traversal Type:")
            print("1. Inorder")
            print("2. Preorder")
            print("3. Postorder")
            t_choice = input("Enter traversal choice (1-3): ").strip()
           
            if tree.root is None:
                print("No log entries found.")
            else:
                if t_choice == '1':
                    print("\n--- Inorder Traversal ---")
                    tree.inorder(tree.root)
                elif t_choice == '2':
                    print("\n--- Preorder Traversal ---")
                    tree.preorder(tree.root)
                elif t_choice == '3':
                    print("\n--- Postorder Traversal ---")
                    tree.postorder(tree.root)
                else:
                    print("Invalid traversal choice.")
                   
        elif choice == '5':
            total = tree.count(tree.root)
            print(f"Total entries in log book: {total}")
            display_logs(tree)
           
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select between 1 and 6.")


if __name__ == "__main__":
    main()
