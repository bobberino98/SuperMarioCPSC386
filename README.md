# SuperMarioCPSC386

A take on classic Super Mario. For educational purposes.

Art:
	
	Place clouds and background hills
	Place blocks( question and normal)
	Render ground
	Place pipes
	Place enemies
	Mario running (3 frames, left and right, plus a frame for sharp turning)
	Mario Jumping(2 frames, left and right, plus a turning frame)
	Mario growing
	Mario shrinking
	Big Mario(3 more, left and right, plus turning and crouching, 1 frame each)
	Fire Mario( same as above)
	Fireball
	Background(flat blue, plus 3 sizes of cloud, Hills and Bushes)
	Blocks(question mark and normal)
	Coins
	Power ups (mushroom and animated flower)
	Brick ground(1 tile, repeated across the screen)
	Pipes(top tile and middle tile, to make varying heights)
	Goomba walking(2 frames, plus death)
	Koopa(2 frames + shell)
	Mario holding a shell
	Flag
	Mario sliding down flag
	Sewer background
	Sewer brick tiles
	Castle

Layout:
	
	Place clouds and background hills/bushes
	Place blocks( question and normal)
	Render ground
	Place pipes
	Place enemies

Logic:
	
	Screen scrolling( once mario hits center)
	Mario acceleration
	friction physics
	Mario jumping gravity
	Mario jumping but then holding against the jump
	Mario fireball physics
	Mario collision
	Enemy collision
	Enemy movement/ai
	Enemy death
	Enemy gravity
	Power up collision and physics
	Mario transforming
	Mario death
	Jumping on shells to make them slide
	Score board
	Enemy scores
	Combo scores
	Timer
	Start of map
	End of map(finish)
	Lives
	Sound Effects
	Music

Classes:
	
	Main loop
	State manager
	Sound manager
	Visual object manager
	Mario
	Goomba
	koopa
	Map
	Event
	Game object manager(state of mario, lives, etc)
