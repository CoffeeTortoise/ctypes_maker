DLL_NAME.sfCircleShape_create.restype = ctypes.POINTER(sfCircleShape)
DLL_NAME.sfCircleShape_create.argtypes = [voi]

def sfCircleShape_create(void):	
	'''
	Args:
		void: voi
	Returns:
		ctypes.POINTER(sfCircleShape)
	'''
	return DLL_NAME.sfCircleShape_create(void)


DLL_NAME.sfCircleShape_copy.restype = ctypes.POINTER(sfCircleShape)
DLL_NAME.sfCircleShape_copy.argtypes = [ctypes.POINTER(sfCircleShape)]

def sfCircleShape_copy(shape):	
	'''
	Args:
		shape: ctypes.POINTER(sfCircleShape)
	Returns:
		ctypes.POINTER(sfCircleShape)
	'''
	return DLL_NAME.sfCircleShape_copy(shape)


DLL_NAME.sfCircleShape_destroy.restype = None
DLL_NAME.sfCircleShape_destroy.argtypes = [ctypes.POINTER(sfCircleShape)]

def sfCircleShape_destroy(shape):	
	'''
	Args:
		shape: ctypes.POINTER(sfCircleShape)
	Returns:
		None
	'''
	return DLL_NAME.sfCircleShape_destroy(shape)


DLL_NAME.sfCircleShape_setPosition.restype = None
DLL_NAME.sfCircleShape_setPosition.argtypes = [sfVector2f, ctypes.POINTER(sfCircleShape)]

def sfCircleShape_setPosition(position, shape):	
	'''
	Args:
		position: sfVector2f
		shape: ctypes.POINTER(sfCircleShape)
	Returns:
		None
	'''
	return DLL_NAME.sfCircleShape_setPosition(position, shape)


DLL_NAME.sfCircleShape_setRotation.restype = None
DLL_NAME.sfCircleShape_setRotation.argtypes = [ctypes.POINTER(sfCircleShape), ctypes.c_float]

def sfCircleShape_setRotation(shape, angle):	
	'''
	Args:
		shape: ctypes.POINTER(sfCircleShape)
		angle: ctypes.c_float
	Returns:
		None
	'''
	return DLL_NAME.sfCircleShape_setRotation(shape, angle)


DLL_NAME.sfCircleShape_setScale.restype = None
DLL_NAME.sfCircleShape_setScale.argtypes = [ctypes.POINTER(sfCircleShape), sfVector2f]

def sfCircleShape_setScale(shape, scale):	
	'''
	Args:
		shape: ctypes.POINTER(sfCircleShape)
		scale: sfVector2f
	Returns:
		None
	'''
	return DLL_NAME.sfCircleShape_setScale(shape, scale)


DLL_NAME.sfCircleShape_setOrigin.restype = None
DLL_NAME.sfCircleShape_setOrigin.argtypes = [sfVector2f, ctypes.POINTER(sfCircleShape)]

def sfCircleShape_setOrigin(origin, shape):	
	'''
	Args:
		origin: sfVector2f
		shape: ctypes.POINTER(sfCircleShape)
	Returns:
		None
	'''
	return DLL_NAME.sfCircleShape_setOrigin(origin, shape)


DLL_NAME.sfCircleShape_getPosition.restype = sfVector2f
DLL_NAME.sfCircleShape_getPosition.argtypes = [ctypes.POINTER(sfCircleShape)]

def sfCircleShape_getPosition(shape):	
	'''
	Args:
		shape: ctypes.POINTER(sfCircleShape)
	Returns:
		sfVector2f
	'''
	return DLL_NAME.sfCircleShape_getPosition(shape)


DLL_NAME.sfCircleShape_getRotation.restype = ctypes.c_float
DLL_NAME.sfCircleShape_getRotation.argtypes = [ctypes.POINTER(sfCircleShape)]

def sfCircleShape_getRotation(shape):	
	'''
	Args:
		shape: ctypes.POINTER(sfCircleShape)
	Returns:
		ctypes.c_float
	'''
	return DLL_NAME.sfCircleShape_getRotation(shape)


DLL_NAME.sfCircleShape_getScale.restype = sfVector2f
DLL_NAME.sfCircleShape_getScale.argtypes = [ctypes.POINTER(sfCircleShape)]

def sfCircleShape_getScale(shape):	
	'''
	Args:
		shape: ctypes.POINTER(sfCircleShape)
	Returns:
		sfVector2f
	'''
	return DLL_NAME.sfCircleShape_getScale(shape)


DLL_NAME.sfCircleShape_getOrigin.restype = sfVector2f
DLL_NAME.sfCircleShape_getOrigin.argtypes = [ctypes.POINTER(sfCircleShape)]

def sfCircleShape_getOrigin(shape):	
	'''
	Args:
		shape: ctypes.POINTER(sfCircleShape)
	Returns:
		sfVector2f
	'''
	return DLL_NAME.sfCircleShape_getOrigin(shape)


DLL_NAME.sfCircleShape_move.restype = None
DLL_NAME.sfCircleShape_move.argtypes = [ctypes.POINTER(sfCircleShape), sfVector2f]

def sfCircleShape_move(shape, offset):	
	'''
	Args:
		shape: ctypes.POINTER(sfCircleShape)
		offset: sfVector2f
	Returns:
		None
	'''
	return DLL_NAME.sfCircleShape_move(shape, offset)


DLL_NAME.sfCircleShape_rotate.restype = None
DLL_NAME.sfCircleShape_rotate.argtypes = [ctypes.POINTER(sfCircleShape), ctypes.c_float]

def sfCircleShape_rotate(shape, angle):	
	'''
	Args:
		shape: ctypes.POINTER(sfCircleShape)
		angle: ctypes.c_float
	Returns:
		None
	'''
	return DLL_NAME.sfCircleShape_rotate(shape, angle)


DLL_NAME.sfCircleShape_scale.restype = None
DLL_NAME.sfCircleShape_scale.argtypes = [ctypes.POINTER(sfCircleShape), sfVector2f]

def sfCircleShape_scale(shape, factors):	
	'''
	Args:
		shape: ctypes.POINTER(sfCircleShape)
		factors: sfVector2f
	Returns:
		None
	'''
	return DLL_NAME.sfCircleShape_scale(shape, factors)


DLL_NAME.sfCircleShape_getTransform.restype = sfTransform
DLL_NAME.sfCircleShape_getTransform.argtypes = [ctypes.POINTER(sfCircleShape)]

def sfCircleShape_getTransform(shape):	
	'''
	Args:
		shape: ctypes.POINTER(sfCircleShape)
	Returns:
		sfTransform
	'''
	return DLL_NAME.sfCircleShape_getTransform(shape)


DLL_NAME.sfCircleShape_getInverseTransform.restype = sfTransform
DLL_NAME.sfCircleShape_getInverseTransform.argtypes = [ctypes.POINTER(sfCircleShape)]

def sfCircleShape_getInverseTransform(shape):	
	'''
	Args:
		shape: ctypes.POINTER(sfCircleShape)
	Returns:
		sfTransform
	'''
	return DLL_NAME.sfCircleShape_getInverseTransform(shape)


DLL_NAME.sfCircleShape_setTexture.restype = None
DLL_NAME.sfCircleShape_setTexture.argtypes = [ctypes.POINTER(sfCircleShape), ctypes.c_int, ctypes.POINTER(sfTexture)]

def sfCircleShape_setTexture(shape, resetRect, texture):	
	'''
	Args:
		shape: ctypes.POINTER(sfCircleShape)
		resetRect: ctypes.c_int
		texture: ctypes.POINTER(sfTexture)
	Returns:
		None
	'''
	return DLL_NAME.sfCircleShape_setTexture(shape, resetRect, texture)


DLL_NAME.sfCircleShape_setTextureRect.restype = None
DLL_NAME.sfCircleShape_setTextureRect.argtypes = [ctypes.POINTER(sfCircleShape), sfIntRect]

def sfCircleShape_setTextureRect(shape, rect):	
	'''
	Args:
		shape: ctypes.POINTER(sfCircleShape)
		rect: sfIntRect
	Returns:
		None
	'''
	return DLL_NAME.sfCircleShape_setTextureRect(shape, rect)


DLL_NAME.sfCircleShape_setFillColor.restype = None
DLL_NAME.sfCircleShape_setFillColor.argtypes = [sfColor, ctypes.POINTER(sfCircleShape)]

def sfCircleShape_setFillColor(color, shape):	
	'''
	Args:
		color: sfColor
		shape: ctypes.POINTER(sfCircleShape)
	Returns:
		None
	'''
	return DLL_NAME.sfCircleShape_setFillColor(color, shape)


DLL_NAME.sfCircleShape_setOutlineColor.restype = None
DLL_NAME.sfCircleShape_setOutlineColor.argtypes = [sfColor, ctypes.POINTER(sfCircleShape)]

def sfCircleShape_setOutlineColor(color, shape):	
	'''
	Args:
		color: sfColor
		shape: ctypes.POINTER(sfCircleShape)
	Returns:
		None
	'''
	return DLL_NAME.sfCircleShape_setOutlineColor(color, shape)


DLL_NAME.sfCircleShape_setOutlineThickness.restype = None
DLL_NAME.sfCircleShape_setOutlineThickness.argtypes = [ctypes.POINTER(sfCircleShape), ctypes.c_float]

def sfCircleShape_setOutlineThickness(shape, thickness):	
	'''
	Args:
		shape: ctypes.POINTER(sfCircleShape)
		thickness: ctypes.c_float
	Returns:
		None
	'''
	return DLL_NAME.sfCircleShape_setOutlineThickness(shape, thickness)


DLL_NAME.sfCircleShape_getTexture.restype = ctypes.POINTER(sfTexture)
DLL_NAME.sfCircleShape_getTexture.argtypes = [ctypes.POINTER(sfCircleShape)]

def sfCircleShape_getTexture(shape):	
	'''
	Args:
		shape: ctypes.POINTER(sfCircleShape)
	Returns:
		ctypes.POINTER(sfTexture)
	'''
	return DLL_NAME.sfCircleShape_getTexture(shape)


DLL_NAME.sfCircleShape_getTextureRect.restype = sfIntRect
DLL_NAME.sfCircleShape_getTextureRect.argtypes = [ctypes.POINTER(sfCircleShape)]

def sfCircleShape_getTextureRect(shape):	
	'''
	Args:
		shape: ctypes.POINTER(sfCircleShape)
	Returns:
		sfIntRect
	'''
	return DLL_NAME.sfCircleShape_getTextureRect(shape)


DLL_NAME.sfCircleShape_getFillColor.restype = sfColor
DLL_NAME.sfCircleShape_getFillColor.argtypes = [ctypes.POINTER(sfCircleShape)]

def sfCircleShape_getFillColor(shape):	
	'''
	Args:
		shape: ctypes.POINTER(sfCircleShape)
	Returns:
		sfColor
	'''
	return DLL_NAME.sfCircleShape_getFillColor(shape)


DLL_NAME.sfCircleShape_getOutlineColor.restype = sfColor
DLL_NAME.sfCircleShape_getOutlineColor.argtypes = [ctypes.POINTER(sfCircleShape)]

def sfCircleShape_getOutlineColor(shape):	
	'''
	Args:
		shape: ctypes.POINTER(sfCircleShape)
	Returns:
		sfColor
	'''
	return DLL_NAME.sfCircleShape_getOutlineColor(shape)


DLL_NAME.sfCircleShape_getOutlineThickness.restype = ctypes.c_float
DLL_NAME.sfCircleShape_getOutlineThickness.argtypes = [ctypes.POINTER(sfCircleShape)]

def sfCircleShape_getOutlineThickness(shape):	
	'''
	Args:
		shape: ctypes.POINTER(sfCircleShape)
	Returns:
		ctypes.c_float
	'''
	return DLL_NAME.sfCircleShape_getOutlineThickness(shape)


DLL_NAME.sfCircleShape_getPointCount.restype = ctypes.c_ulonglong
DLL_NAME.sfCircleShape_getPointCount.argtypes = [ctypes.POINTER(sfCircleShape)]

def sfCircleShape_getPointCount(shape):	
	'''
	Args:
		shape: ctypes.POINTER(sfCircleShape)
	Returns:
		ctypes.c_ulonglong
	'''
	return DLL_NAME.sfCircleShape_getPointCount(shape)


DLL_NAME.sfCircleShape_getPoint.restype = sfVector2f
DLL_NAME.sfCircleShape_getPoint.argtypes = [ctypes.c_ulonglong, ctypes.POINTER(sfCircleShape)]

def sfCircleShape_getPoint(index, shape):	
	'''
	Args:
		index: ctypes.c_ulonglong
		shape: ctypes.POINTER(sfCircleShape)
	Returns:
		sfVector2f
	'''
	return DLL_NAME.sfCircleShape_getPoint(index, shape)


DLL_NAME.sfCircleShape_setRadius.restype = None
DLL_NAME.sfCircleShape_setRadius.argtypes = [ctypes.POINTER(sfCircleShape), ctypes.c_float]

def sfCircleShape_setRadius(shape, radius):	
	'''
	Args:
		shape: ctypes.POINTER(sfCircleShape)
		radius: ctypes.c_float
	Returns:
		None
	'''
	return DLL_NAME.sfCircleShape_setRadius(shape, radius)


DLL_NAME.sfCircleShape_getRadius.restype = ctypes.c_float
DLL_NAME.sfCircleShape_getRadius.argtypes = [ctypes.POINTER(sfCircleShape)]

def sfCircleShape_getRadius(shape):	
	'''
	Args:
		shape: ctypes.POINTER(sfCircleShape)
	Returns:
		ctypes.c_float
	'''
	return DLL_NAME.sfCircleShape_getRadius(shape)


DLL_NAME.sfCircleShape_setPointCount.restype = None
DLL_NAME.sfCircleShape_setPointCount.argtypes = [ctypes.c_ulonglong, ctypes.POINTER(sfCircleShape)]

def sfCircleShape_setPointCount(count, shape):	
	'''
	Args:
		count: ctypes.c_ulonglong
		shape: ctypes.POINTER(sfCircleShape)
	Returns:
		None
	'''
	return DLL_NAME.sfCircleShape_setPointCount(count, shape)


DLL_NAME.sfCircleShape_getLocalBounds.restype = sfFloatRect
DLL_NAME.sfCircleShape_getLocalBounds.argtypes = [ctypes.POINTER(sfCircleShape)]

def sfCircleShape_getLocalBounds(shape):	
	'''
	Args:
		shape: ctypes.POINTER(sfCircleShape)
	Returns:
		sfFloatRect
	'''
	return DLL_NAME.sfCircleShape_getLocalBounds(shape)


DLL_NAME.sfCircleShape_getGlobalBounds.restype = sfFloatRect
DLL_NAME.sfCircleShape_getGlobalBounds.argtypes = [ctypes.POINTER(sfCircleShape)]

def sfCircleShape_getGlobalBounds(shape):	
	'''
	Args:
		shape: ctypes.POINTER(sfCircleShape)
	Returns:
		sfFloatRect
	'''
	return DLL_NAME.sfCircleShape_getGlobalBounds(shape)

