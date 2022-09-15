public class CCullingManager
{
//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void Unregister(CullingHandle h)
	{
	#if COUNT_SHOWING_SPHERE
		if (((CGraphicObjectInstance)h.GetUserData()).isShow())
		{
			Tracef("DE : %p  ",h.GetUserData());
			showingcount--;
			Tracef("show size : %5d\n",showingcount);
		}
	#endif
		m_Factory.Remove(h);
	}
}