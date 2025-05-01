def subject_marks(subjectmarks):
    # Sort the list of tuples based on the second element (marks) in descending order
    sorted_subjectmarks = sorted(subjectmarks, key=lambda x: x[1], reverse=True)
    return sorted_subjectmarks