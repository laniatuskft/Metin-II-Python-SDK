public class Vector3d : D3DXVECTOR3
{
	public Vector3d()
	{
	}

	public Vector3d(in Vector3d a)
	{
		x = a.x;
		y = a.y;
		z = a.z;
	}

	public Vector3d(float a, float b, float c)
	{
		x = a;
		y = b;
		z = c;
	}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: bool operator ==(const Vector3d &a) const
	public static bool operator == (Vector3d ImpliedObject, in Vector3d a)
	{
		if (a.x == x && a.y == y && a.z == z)
		{
			return true;
		}
		return false;
	}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: bool operator !=(const Vector3d &a) const
	public static bool operator != (Vector3d ImpliedObject, in Vector3d a)
	{
		if (a.x != x || a.y != y || a.z != z)
		{
			return true;
		}
		return false;
	}

//# Laniatus Games Studio Inc. |: This 'CopyFrom' method was converted from the original copy assignment operator:
//Original Metin2 CPlus Line: Vector3d& operator = (const Vector3d& A)
	public Vector3d CopyFrom (in Vector3d A)
	{
		x = A.x;
		y = A.y;
		z = A.z;
	return (this);
	}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: Vector3d operator + (const Vector3d& A) const
	public static Vector3d operator + (Vector3d ImpliedObject, in Vector3d A)
	{
		Vector3d Sum = new ImpliedObject.Vector3d(x + A.x, y + A.y, z + A.z);
	return (Sum);
	}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: Vector3d operator - (const Vector3d& A) const
	public static Vector3d operator - (Vector3d ImpliedObject, in Vector3d A)
	{
		Vector3d Diff = new ImpliedObject.Vector3d(x - A.x, y - A.y, z - A.z);
	return (Diff);
	}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: Vector3d operator * (const float s) const
	public static Vector3d operator * (Vector3d ImpliedObject, in float s)
	{
		Vector3d Scaled = new ImpliedObject.Vector3d(x * s, y * s, z * s);
	return (Scaled);
	}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: Vector3d operator / (const float s) const
	public static Vector3d operator / (Vector3d ImpliedObject, in float s)
	{
		float r = 1.0f / s;
		Vector3d Scaled = new ImpliedObject.Vector3d(x * r, y * r, z * r);
		return (Scaled);
	}

//# Laniatus Games Studio Inc. | TODO TASK: The += operator cannot be overloaded in C#:
	public static void operator += (in Vector3d A)
	{
		x += A.x;
		y += A.y;
		z += A.z;
	}
//# Laniatus Games Studio Inc. | TODO TASK: The -= operator cannot be overloaded in C#:
	public static void operator -= (in Vector3d A)
	{
		x -= A.x;
		y -= A.y;
		z -= A.z;
	}
//# Laniatus Games Studio Inc. | TODO TASK: The *= operator cannot be overloaded in C#:
	public static void operator *= (in float s)
	{
		x *= s;
		y *= s;
		z *= s;
	}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: Vector3d operator - () const
	public static Vector3d operator - (Vector3d ImpliedObject)
	{
		Vector3d Negated = new ImpliedObject.Vector3d(-x, -y, -z);
	return (Negated);
	}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: float operator [] (const int i) const
	public float this [in int i]
	{
		get
		{
			return ((i == 0)?x:((i == 1)?y:z));
		}
	}
	public float this [in int i]
	{
		get
		{
			return ((i == 0)?x:((i == 1)?y:z));
		}
		set
		{
			((i == 0)?x:((i == 1)?y:z)) = value;
		}
	}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: float GetX() const
	public float GetX()
	{
		return x;
	}
//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: float GetY() const
	public float GetY()
	{
		return y;
	}
//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: float GetZ() const
	public float GetZ()
	{
		return z;
	}

	public void SetX(float t)
	{
		x = t;
	}
	public void SetY(float t)
	{
		y = t;
	}
	public void SetZ(float t)
	{
		z = t;
	}

	public void Set(float a, float b, float c)
	{
		x = a;
		y = b;
		z = c;
	}

	public void Zero()
	{
		x = y = z = 0;
	}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: Vector3d negative() const
	public Vector3d negative()
	{
		Vector3d result = new Vector3d();
		result.x = -x;
		result.y = -y;
		result.z = -z;
		return new Vector3d(result);
	}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: float Magnitude() const
	public float Magnitude()
	{
		return (sqrtf(x * x + y * y + z * z));
	}

	public void Lerp(in Vector3d from, in Vector3d to, float slerp)
	{
		this = to - from;
		this *= slerp;
		this += from;
	}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: float Length() const
	public float Length()
	{
		return (float)sqrtf(x * x + y * y + z * z);
	}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: float Length2() const
	public float Length2()
	{
		float l2 = x * x + y * y + z * z;
		return l2;
	}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: inline float Distance(const Vector3d &a) const
	public float Distance(in Vector3d a)
	{
		return sqrtf(DistanceSq(a));
	}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: inline float Distance2d(const Vector3d &a) const
	public float Distance2d(in Vector3d a)
	{
		return sqrtf(DistanceSq2d(a));
	}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: float DistanceXY(const Vector3d &a) const
	public float DistanceXY(in Vector3d a)
	{
		float dx = a.x - x;
		float dy = a.y - y;
		float dist = dx * dx + dy * dy;
		return dist;
	}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: float DistanceSq(const Vector3d &a) const
	public float DistanceSq(in Vector3d a)
	{
		float dx = a.x - x;
		float dy = a.y - y;
		float dz = a.z - z;
		return dx * dx + dy * dy + dz * dz;
	}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: float DistanceSq2d(const Vector3d &a) const
	public float DistanceSq2d(in Vector3d a)
	{
		float dx = a.x - x;
		float dy = a.y - y;
		return dx * dx + dy * dy;
	}

	public float Normalize()
	{
		float l = Length();
		if (l != 0F)
		{
			x /= l;
			y /= l;
			z /= l;
		}
		else
		{
			x = y = z = 0;
		}
		return l;
	}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: float Dot(const Vector3d &a) const
	public float Dot(in Vector3d a)
	{
		return (x * a.x + y * a.y + z * a.z);
	}
//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: bool IsInStaticRange() const;
	public bool IsInStaticRange()
	{
		const float LIMIT = 3276700.0f;
		if (x < LIMIT && x>-LIMIT)
		{
			if (y < LIMIT && y>-LIMIT)
			{
				if (z < LIMIT && z>-LIMIT)
				{
					return true;
				}
			}
		}
    
		return false;
	}
	public void Cross(in Vector3d a, in Vector3d b)
	{
		x = a.y * b.z - a.z * b.y;
		y = a.z * b.x - a.x * b.z;
		z = a.x * b.y - a.y * b.x;
	}
}