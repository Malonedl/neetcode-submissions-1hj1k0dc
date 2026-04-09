class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # sandwiches = stack
        # students = queue
        # if they dont like the sandwich at top of stack, move current forward, and make that student the new tail
        # if they like the sandwhich  dequeue them and remove the sandwhich from the stack 
        # repeat until all sandwiches are taken or no one will take the top sandwich 

        circularStudents = 0
        squareStudents = 0

        # get a count of the students preference 
        for j in students:
            if j == 0:
                circularStudents += 1
            
            else: 
                squareStudents += 1

        for i in sandwiches:
            if i == 0 and circularStudents > 0:
                circularStudents -= 1

            
            elif i == 1 and squareStudents > 0:
                squareStudents -= 1
            
            else: 
                return (squareStudents + circularStudents)

        return 0