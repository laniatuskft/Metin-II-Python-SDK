public class IAbstractApplication : TAbstractSingleton<IAbstractApplication>
{
		public class SCameraPos
		{
			public float m_fUpDir;
			public float m_fViewDir;
			public float m_fCrossDir;

			public SCameraPos()
			{
				this.m_fUpDir = 0.0f;
				this.m_fViewDir = 0.0f;
				this.m_fCrossDir = 0.0f;
			}
		}

		public class SCameraSetting
		{
			public D3DXVECTOR3 v3CenterPosition = new D3DXVECTOR3();
			public SCameraPos kCmrPos = new SCameraPos();
			public float fRotation;
			public float fPitch;
			public float fZoom;

			public SCameraSetting()
			{
				this.v3CenterPosition = new D3DXVECTOR3(0.0f, 0.0f, 0.0f);
				this.fRotation = 0.0f;
				this.fPitch = 0.0f;
				this.fZoom = 0.0f;
			}
		}

		public IAbstractApplication()
		{
		}
		public virtual void Dispose()
		{
		}

		public abstract void GetMousePosition(POINT ppt);
		public abstract float GetGlobalTime();
		public abstract float GetGlobalElapsedTime();

		public abstract void SkipRenderBuffering(uint dwSleepMSec);
		public abstract void SetServerTime(time_t tTime);
		public abstract void SetCenterPosition(float fx, float fy, float fz);

		public abstract void SetEventCamera(in SCameraSetting c_rCameraSetting);
		public abstract void BlendEventCamera(in SCameraSetting c_rCameraSetting, float fBlendTime);
		public abstract void SetDefaultCamera();

		public abstract void RunIMEUpdate();
		public abstract void RunIMETabEvent();
		public abstract void RunIMEReturnEvent();

		public abstract void RunIMEChangeCodePage();
		public abstract void RunIMEOpenCandidateListEvent();
		public abstract void RunIMECloseCandidateListEvent();
		public abstract void RunIMEOpenReadingWndEvent();
		public abstract void RunIMECloseReadingWndEvent();
}