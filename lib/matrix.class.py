# Generates the game grid and handles interactions with it
class Matrix:
	# Game grid
	grid = []
	
	# Generates game grid on matrix initialisation
	def __init__(self, mWidth, mHeight):
		for y in range(0, mHeight):
			row = []
			
			for x in range(0, mWidth):
				row.append(0)
			
			self.grid.append(row)
	
	# Returns if a wall exists at the given position
	def isWall(self,xPos, yPos):
		if self.grid[yPos][xPos] == 1:
			return True
		else:
			return False