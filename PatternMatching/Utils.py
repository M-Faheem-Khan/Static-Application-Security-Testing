class Utils:
    def print_error(self, className, classMethod, error, usage):
        print(f"{className}.{classMethod} - {error}\nUsage: {usage}")
    
    def print_findings(self, findings):
        if findings == []:
            print("No issues found.")
        else:
            print(f"=== Identified {len(findings)} issues. ===\n")
            for finding in findings:
                print(f"Description: {finding["description"]}")
                print(f"Source: {finding["file_path"]}@L{finding["line_number"]}: {finding["line_content"]}")
                print("")
