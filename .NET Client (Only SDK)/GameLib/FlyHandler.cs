public class IFlyEventHandler : System.IDisposable
{
	public IFlyEventHandler()
	{
	}
	public virtual void Dispose()
	{
	}
	public virtual void OnSetFlyTarget()
	{
	}
	public virtual void OnShoot(uint dwSkillIndex)
	{
	}
	public virtual void OnNoTarget()
	{
	}
	public virtual void OnNoArrow()
	{
	}
	public virtual void OnExplodingOutOfRange()
	{
	}
	public virtual void OnExplodingAtBackground()
	{
	}
	public virtual void OnExplodingAtAnotherTarget(uint dwSkillIndex, uint dwVID)
	{
	}
	public virtual void OnExplodingAtTarget(uint dwSkillIndex)
	{
	}
}