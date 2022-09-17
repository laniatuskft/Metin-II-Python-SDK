public class CGrannyModelInstance
{
//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void MakeBoundBox(TBoundBox pBoundBox, float[] mat, float[] OBBMin, float[] OBBMax, D3DXVECTOR3 vtMin, D3DXVECTOR3 vtMax)
	{
		pBoundBox.sx = OBBMin[0] * mat[0] + OBBMin[1] * mat[4] + OBBMin[2] * mat[8] + mat[12];
		pBoundBox.sy = OBBMin[0] * mat[1] + OBBMin[1] * mat[5] + OBBMin[2] * mat[9] + mat[13];
		pBoundBox.sz = OBBMin[0] * mat[2] + OBBMin[1] * mat[6] + OBBMin[2] * mat[10] + mat[14];
    
		pBoundBox.ex = OBBMax[0] * mat[0] + OBBMax[1] * mat[4] + OBBMax[2] * mat[8] + mat[12];
		pBoundBox.ey = OBBMax[0] * mat[1] + OBBMax[1] * mat[5] + OBBMax[2] * mat[9] + mat[13];
		pBoundBox.ez = OBBMax[0] * mat[2] + OBBMax[1] * mat[6] + OBBMax[2] * mat[10] + mat[14];
    
		vtMin.x = Math.Min(vtMin.x, pBoundBox.sx);
		vtMin.x = Math.Min(vtMin.x, pBoundBox.ex);
		vtMin.y = Math.Min(vtMin.y, pBoundBox.sy);
		vtMin.y = Math.Min(vtMin.y, pBoundBox.ey);
		vtMin.z = Math.Min(vtMin.z, pBoundBox.sz);
		vtMin.z = Math.Min(vtMin.z, pBoundBox.ez);
    
		vtMax.x = Math.Max(vtMax.x, pBoundBox.sx);
		vtMax.x = Math.Max(vtMax.x, pBoundBox.ex);
		vtMax.y = Math.Max(vtMax.y, pBoundBox.sy);
		vtMax.y = Math.Max(vtMax.y, pBoundBox.ey);
		vtMax.z = Math.Max(vtMax.z, pBoundBox.sz);
		vtMax.z = Math.Max(vtMax.z, pBoundBox.ez);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool Intersect(D3DXMATRIX c_pMatrix, ref float UnnamedParameter, ref float UnnamedParameter2, ref float pt)
	{
		if (!m_pgrnModelInstance)
		{
			return false;
		}
    
		float u;
		float v;
		float t;
		bool ret = false;
		pt = 100000000.0f;
    
		float max = 10000000.0f;
		D3DXVECTOR3 vtMin = new D3DXVECTOR3();
		D3DXVECTOR3 vtMax = new D3DXVECTOR3();
		vtMin.x = vtMin.y = vtMin.z = max;
		vtMax.x = vtMax.y = vtMax.z = -max;
    
	//# Laniatus Games Studio Inc. |: This static local variable declaration (not allowed in C#) has been moved just prior to the method:
	//	static stl_stack_pool<TBoundBox> s_boundBoxPool(1024);
		Intersect_s_boundBoxPool.clear();
    
		int meshCount = m_pModel.GetMeshCount();
    
		for (int m = 0; m < meshCount; ++m)
		{
			granny_mesh pgrnMesh = m_pModel.GetGrannyModelPointer().MeshBindings[m].Mesh;
    
			for (int b = 0; b < pgrnMesh.BoneBindingCount; ++b)
			{
				granny_bone_binding rgrnBoneBinding = pgrnMesh.BoneBindings[b];
    
				TBoundBox pBoundBox = Intersect_s_boundBoxPool.alloc();
    
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not have an equivalent to pointers to value types:
	//Original Metin2 CPlus Line: float * Transform = GrannyGetWorldPose4x4(__GetWorldPosePtr(), __GetMeshBoneIndices m[b]);
				float Transform = GrannyGetWorldPose4x4(__GetWorldPosePtr(), __GetMeshBoneIndices m[b]);
    
				MakeBoundBox(pBoundBox, Transform, rgrnBoneBinding.OBBMin, rgrnBoneBinding.OBBMax, vtMin, vtMax);
    
				pBoundBox.meshIndex = m;
				pBoundBox.boneIndex = b;
			}
		}
    
		if (!IntersectCube(c_pMatrix, vtMin.x, vtMin.y, vtMin.z, vtMax.x, vtMax.y, vtMax.z, ms_vtPickRayOrig, ms_vtPickRayDir, u, v, t))
		{
			return ret;
		}
    
		return true;
    
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void GetBoundBox(D3DXVECTOR3 vtMin, D3DXVECTOR3 vtMax)
	{
		if (!m_pgrnModelInstance)
		{
			return;
		}
    
		TBoundBox BoundBox = new TBoundBox();
    
		vtMin.x = vtMin.y = vtMin.z = +100000.0f;
		vtMax.x = vtMax.y = vtMax.z = -100000.0f;
    
		int meshCount = m_pModel.GetMeshCount();
		for (int m = 0; m < meshCount; ++m)
		{
			granny_mesh pgrnMesh = m_pModel.GetGrannyModelPointer().MeshBindings[m].Mesh;
			int[] boneIndices = __GetMeshBoneIndices(m);
    
			for (int b = 0; b < pgrnMesh.BoneBindingCount; ++b)
			{
				granny_bone_binding rgrnBoneBinding = pgrnMesh.BoneBindings[b];
    
				MakeBoundBox(BoundBox, GrannyGetWorldPose4x4(__GetWorldPosePtr(), boneIndices[b]), rgrnBoneBinding.OBBMin, rgrnBoneBinding.OBBMax, vtMin, vtMax);
			}
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool GetMeshMatrixPointer(int iMesh, D3DXMATRIX[] c_ppMatrix)
	{
		if (!m_pgrnModelInstance)
		{
			return false;
		}
    
		int meshCount = m_pModel.GetMeshCount();
    
		if (meshCount <= 0)
		{
			return false;
		}
    
	//# Laniatus Games Studio Inc. | TODO TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'CopyFrom' method should be created:
	//Original Metin2 CPlus Line: *c_ppMatrix = (D3DXMATRIX *)GrannyGetWorldPose4x4(__GetWorldPosePtr(), __GetMeshBoneIndices iMesh[0]);
		c_ppMatrix[0].CopyFrom((D3DXMATRIX)GrannyGetWorldPose4x4(__GetWorldPosePtr(), __GetMeshBoneIndices iMesh[0]));
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void Clear()
	{
		m_kMtrlPal.Clear();
    
		DestroyDeviceObjects();
		__DestroyMeshBindingVector();
		__DestroyMeshMatrices();
		__DestroyModelInstance();
		__DestroyWorldPose();
    
		__Initialize();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetMainModelPointer(CGrannyModel pModel, CGraphicVertexBuffer pkSharedDeformableVertexBuffer)
	{
		SetLinkedModelPointer(pModel, pkSharedDeformableVertexBuffer, null);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetLinkedModelPointer(CGrannyModel pkModel, CGraphicVertexBuffer pkSharedDeformableVertexBuffer, CGrannyModelInstance[] ppkSkeletonInst)
	{
		Clear();
    
		if (m_pModel)
		{
			m_pModel.Release();
		}
    
		m_pModel = pkModel;
    
		m_pModel.AddReference();
    
		if (pkSharedDeformableVertexBuffer != null)
		{
			__SetSharedDeformableVertexBuffer(pkSharedDeformableVertexBuffer);
		}
		else
		{
			__CreateDynamicVertexBuffer();
		}
    
		__CreateModelInstance();
    
		if (ppkSkeletonInst && ppkSkeletonInst[0] != null)
		{
			m_ppkSkeletonInst = ppkSkeletonInst;
			__CreateWorldPoseppkSkeletonInst;
			__CreateMeshBindingVectorppkSkeletonInst;
		}
		else
		{
			__CreateWorldPose(null);
			__CreateMeshBindingVector(null);
		}
    
		__CreateMeshMatrices();
    
		ResetLocalTime();
    
		m_kMtrlPal.Copy(pkModel.GetMaterialPalette());
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public granny_world_pose __GetWorldPosePtr()
	{
		if (m_pgrnWorldPoseReal)
		{
			return m_pgrnWorldPoseReal;
		}
    
		if (m_ppkSkeletonInst && *m_ppkSkeletonInst)
		{
			return m_ppkSkeletonInst.m_pgrnWorldPoseReal;
		}
    
		Debug.Assert(m_ppkSkeletonInst != null && "__GetWorldPosePtr - NO HAVE SKELETON");
		return null;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public int __GetMeshBoneIndices(uint iMeshBinding)
	{
		Debug.Assert(iMeshBinding < m_vct_pgrnMeshBinding.size());
		return (int)GrannyGetMeshBindingToBoneIndices(m_vct_pgrnMeshBinding[iMeshBinding]);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool __CreateMeshBindingVector(CGrannyModelInstance pkDstModelInst)
	{
		Debug.Assert(m_vct_pgrnMeshBinding.empty());
    
		if (!m_pModel)
		{
			return false;
		}
    
		granny_model pgrnModel = m_pModel.GetGrannyModelPointer();
		if (pgrnModel == null)
		{
			return false;
		}
    
		granny_skeleton pgrnDstSkeleton = pgrnModel.Skeleton;
		if (pkDstModelInst != null && pkDstModelInst.m_pModel && pkDstModelInst.m_pModel.GetGrannyModelPointer())
		{
			pgrnDstSkeleton = pkDstModelInst.m_pModel.GetGrannyModelPointer().Skeleton;
		}
    
		m_vct_pgrnMeshBinding.reserve(pgrnModel.MeshBindingCount);
    
		int iMeshBinding;
		for (iMeshBinding = 0; iMeshBinding != pgrnModel.MeshBindingCount; ++iMeshBinding)
		{
			m_vct_pgrnMeshBinding.push_back(GrannyNewMeshBinding(pgrnModel.MeshBindings[iMeshBinding].Mesh, pgrnModel.Skeleton, pgrnDstSkeleton));
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __DestroyMeshBindingVector()
	{
		std::for_each(m_vct_pgrnMeshBinding.begin(), m_vct_pgrnMeshBinding.end(), GrannyFreeMeshBinding);
		m_vct_pgrnMeshBinding.clear();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __CreateWorldPose(CGrannyModelInstance pkSkeletonInst)
	{
		Debug.Assert(m_pgrnModelInstance != null);
		Debug.Assert(m_pgrnWorldPoseReal == null);
    
		if (pkSkeletonInst != null)
		{
			return;
		}
    
		granny_skeleton pgrnSkeleton = GrannyGetSourceSkeleton(m_pgrnModelInstance);
    
		m_pgrnWorldPoseReal = GrannyNewWorldPose(pgrnSkeleton.BoneCount);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __DestroyWorldPose()
	{
		if (!m_pgrnWorldPoseReal)
		{
			return;
		}
    
		GrannyFreeWorldPose(m_pgrnWorldPoseReal);
		m_pgrnWorldPoseReal = null;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __CreateModelInstance()
	{
		Debug.Assert(m_pModel != null);
		Debug.Assert(m_pgrnModelInstance == null);
    
		granny_model pgrnModel = m_pModel.GetGrannyModelPointer();
		m_pgrnModelInstance = GrannyInstantiateModel(pgrnModel);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __DestroyModelInstance()
	{
		if (!m_pgrnModelInstance)
		{
			return;
		}
    
		GrannyFreeModelInstance(m_pgrnModelInstance);
		m_pgrnModelInstance = null;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __CreateMeshMatrices()
	{
		Debug.Assert(m_pModel != null);
    
		if (m_pModel.GetMeshCount() <= 0)
		{
			return;
		}
    
		int meshCount = m_pModel.GetMeshCount();
		m_meshMatrices = Arrays.InitializeWithDefaultInstances<D3DXMATRIX>(meshCount);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __DestroyMeshMatrices()
	{
		if (!m_meshMatrices)
		{
			return;
		}
    
		m_meshMatrices = null;
		m_meshMatrices = null;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public uint GetDeformableVertexCount()
	{
		if (!m_pModel)
		{
			return 0;
		}
    
		return m_pModel.GetDeformVertexCount();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public uint GetVertexCount()
	{
		if (!m_pModel)
		{
			return 0;
		}
    
		return m_pModel.GetVertexCount();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __SetSharedDeformableVertexBuffer(CGraphicVertexBuffer pkSharedDeformableVertexBuffer)
	{
		m_pkSharedDeformableVertexBuffer = pkSharedDeformableVertexBuffer;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool __IsDeformableVertexBuffer()
	{
		if (m_pkSharedDeformableVertexBuffer)
		{
			return true;
		}
    
		return m_kLocalDeformableVertexBuffer.IsEmpty();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public IDirect3DVertexBuffer8 __GetDeformableD3DVertexBufferPtr()
	{
		return __GetDeformableVertexBufferRef().GetD3DVertexBuffer();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public CGraphicVertexBuffer __GetDeformableVertexBufferRef()
	{
		if (m_pkSharedDeformableVertexBuffer)
		{
			return m_pkSharedDeformableVertexBuffer;
		}
    
		return m_kLocalDeformableVertexBuffer;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __CreateDynamicVertexBuffer()
	{
		Debug.Assert(m_pModel != null);
		Debug.Assert(m_kLocalDeformableVertexBuffer.IsEmpty());
    
		int vtxCount = m_pModel.GetDeformVertexCount();
    
		if (0 != vtxCount)
		{
			if (!m_kLocalDeformableVertexBuffer.Create(vtxCount, D3DFVF_XYZ | D3DFVF_NORMAL | D3DFVF_TEX1, D3DUSAGE_WRITEONLY, D3DPOOL_MANAGED))
			{
				return;
			}
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __DestroyDynamicVertexBuffer()
	{
		m_kLocalDeformableVertexBuffer.Destroy();
		m_pkSharedDeformableVertexBuffer = null;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool GetBoneIndexByName(string c_szBoneName, ref int pBoneIndex)
	{
		Debug.Assert(m_pgrnModelInstance != null);
    
		granny_skeleton pgrnSkeleton = GrannyGetSourceSkeleton(m_pgrnModelInstance);
    
		if (!GrannyFindBoneByName(pgrnSkeleton, c_szBoneName, pBoneIndex))
		{
			return false;
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public float GetBoneMatrixPointer(int iBone)
	{
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not have an equivalent to pointers to value types:
	//Original Metin2 CPlus Line: const float* bones = GrannyGetWorldPose4x4(__GetWorldPosePtr(), iBone);
		float bones = GrannyGetWorldPose4x4(__GetWorldPosePtr(), iBone);
		if (bones == 0)
		{
			granny_model pModel = m_pModel.GetGrannyModelPointer();
			return null;
		}
		return bones;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public float GetCompositeBoneMatrixPointer(int iBone)
	{
		return GrannyGetWorldPoseComposite4x4(__GetWorldPosePtr(), iBone);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ReloadTexture()
	{
		Debug.Assert("???? ??????? ???? - CGrannyModelInstance::ReloadTexture()");
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void CopyMotion(CGrannyModelInstance pModelInstance, bool bIsFreeSourceControl)
	{
		if (!pModelInstance.IsMotionPlaying())
		{
			return;
		}
    
		if (m_pgrnCtrl)
		{
			GrannyFreeControl(m_pgrnCtrl);
		}
    
		float localTime = GetLocalTime();
		m_pgrnAni = pModelInstance.m_pgrnAni;
		m_pgrnCtrl = GrannyPlayControlledAnimation(localTime, m_pgrnAni, m_pgrnModelInstance);
    
		if (!m_pgrnCtrl)
		{
			return;
		}
    
		GrannySetControlSpeed(m_pgrnCtrl, GrannyGetControlSpeed(pModelInstance.m_pgrnCtrl));
		GrannySetControlLoopCount(m_pgrnCtrl, GrannyGetControlLoopCount(pModelInstance.m_pgrnCtrl));
    
		GrannySetControlEaseIn(m_pgrnCtrl, true);
		GrannySetControlEaseOut(m_pgrnCtrl, false);
    
		GrannySetControlRawLocalClock(m_pgrnCtrl, GrannyGetControlRawLocalClock(pModelInstance.m_pgrnCtrl));
    
		GrannyFreeControlOnceUnused(m_pgrnCtrl);
    
		if (bIsFreeSourceControl)
		{
			GrannyFreeControl(pModelInstance.m_pgrnCtrl);
			pModelInstance.m_pgrnCtrl = null;
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool IsMotionPlaying()
	{
		if (!m_pgrnCtrl)
		{
			return false;
		}
    
		if (GrannyControlIsComplete(m_pgrnCtrl))
		{
			return false;
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetMotionPointer(CGrannyMotion pMotion, float blendTime, int loopCount, float speedRatio)
	{
		if (!m_pgrnWorldPoseReal)
		{
			return;
		}
    
		granny_model_instance pgrnModelInstance = m_pgrnModelInstance;
		if (pgrnModelInstance == null)
		{
			return;
		}
    
		float localTime = GetLocalTime();
    
		bool isFirst = false;
		if (m_pgrnCtrl)
		{
			GrannySetControlEaseOutCurve(m_pgrnCtrl, localTime, localTime + blendTime, 1.0f, 1.0f, 0.0f, 0.0f);
			GrannySetControlEaseIn(m_pgrnCtrl, false);
			GrannySetControlEaseOut(m_pgrnCtrl, true);
			GrannyCompleteControlAt(m_pgrnCtrl, localTime + blendTime);
			GrannyFreeControlIfComplete(m_pgrnCtrl);
		}
		else
		{
			isFirst = true;
		}
    
		m_pgrnAni = pMotion.GetGrannyAnimationPointer();
		m_pgrnCtrl = GrannyPlayControlledAnimation(localTime, m_pgrnAni, pgrnModelInstance);
		if (!m_pgrnCtrl)
		{
			return;
		}
    
		GrannySetControlSpeed(m_pgrnCtrl, speedRatio);
		GrannySetControlLoopCount(m_pgrnCtrl, loopCount);
    
		if (isFirst)
		{
			GrannySetControlEaseIn(m_pgrnCtrl, false);
			GrannySetControlEaseOut(m_pgrnCtrl, false);
		}
		else
		{
			GrannySetControlEaseIn(m_pgrnCtrl, true);
			GrannySetControlEaseOut(m_pgrnCtrl, false);
			if (blendTime > 0.0f)
			{
				GrannySetControlEaseInCurve(m_pgrnCtrl, localTime, localTime + blendTime, 0.0f, 0.0f, 1.0f, 1.0f);
			}
		}
		GrannyFreeControlOnceUnused(m_pgrnCtrl);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ChangeMotionPointer(CGrannyMotion pMotion, int loopCount, float speedRatio)
	{
		granny_model_instance pgrnModelInstance = m_pgrnModelInstance;
		if (pgrnModelInstance == null)
		{
			return;
		}
    
		float fSkipTime = 0.3f;
		float localTime = GetLocalTime() - fSkipTime;
    
		if (m_pgrnCtrl)
		{
			GrannySetControlEaseIn(m_pgrnCtrl, false);
			GrannySetControlEaseOut(m_pgrnCtrl, false);
			GrannyCompleteControlAt(m_pgrnCtrl, localTime);
			GrannyFreeControlIfComplete(m_pgrnCtrl);
		}
    
		m_pgrnAni = pMotion.GetGrannyAnimationPointer();
		m_pgrnCtrl = GrannyPlayControlledAnimation(localTime, m_pgrnAni, pgrnModelInstance);
		if (!m_pgrnCtrl)
		{
			return;
		}
    
		GrannySetControlSpeed(m_pgrnCtrl, speedRatio);
		GrannySetControlLoopCount(m_pgrnCtrl, loopCount);
		GrannySetControlEaseIn(m_pgrnCtrl, false);
		GrannySetControlEaseOut(m_pgrnCtrl, false);
    
		GrannyFreeControlOnceUnused(m_pgrnCtrl);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetMotionAtEnd()
	{
		if (!m_pgrnCtrl)
		{
			return;
		}
    
		float endingTime = GrannyGetControlLocalDuration(m_pgrnCtrl);
		GrannySetControlRawLocalClock(m_pgrnCtrl, endingTime);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void DeformNoSkin(_D3DMATRIX c_pWorldMatrix)
	{
		if (IsEmpty())
		{
			return;
		}
    
		UpdateWorldPose();
		UpdateWorldMatrices(c_pWorldMatrix);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void RenderWithOneTexture()
	{
		if (IsEmpty())
		{
			return;
		}
    
    
		STATEMANAGER.SetVertexShader(ms_pntVS);
    
		LPDIRECT3DVERTEXBUFFER8 lpd3dDeformPNTVtxBuf = __GetDeformableD3DVertexBufferPtr();
    
		LPDIRECT3DVERTEXBUFFER8 lpd3dRigidPNTVtxBuf = m_pModel.GetPNTD3DVertexBuffer();
    
		if (lpd3dDeformPNTVtxBuf != null)
		{
			STATEMANAGER.SetStreamSource(0, lpd3dDeformPNTVtxBuf, sizeof(SPNTVertex));
			RenderMeshNodeListWithOneTexture(CGrannyMesh.TYPE_DEFORM, CGrannyMaterial.TYPE_DIFFUSE_PNT);
		}
		if (lpd3dRigidPNTVtxBuf != null)
		{
			STATEMANAGER.SetStreamSource(0, lpd3dRigidPNTVtxBuf, sizeof(SPNTVertex));
			RenderMeshNodeListWithOneTexture(CGrannyMesh.TYPE_RIGID, CGrannyMaterial.TYPE_DIFFUSE_PNT);
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void BlendRenderWithOneTexture()
	{
		if (IsEmpty())
		{
			return;
		}
    
		LPDIRECT3DVERTEXBUFFER8 lpd3dDeformPNTVtxBuf = __GetDeformableD3DVertexBufferPtr();
		LPDIRECT3DVERTEXBUFFER8 lpd3dRigidPNTVtxBuf = m_pModel.GetPNTD3DVertexBuffer();
    
		 STATEMANAGER.SetVertexShader(ms_pntVS);
    
		if (lpd3dDeformPNTVtxBuf != null)
		{
			STATEMANAGER.SetStreamSource(0, lpd3dDeformPNTVtxBuf, sizeof(SPNTVertex));
			RenderMeshNodeListWithOneTexture(CGrannyMesh.TYPE_DEFORM, CGrannyMaterial.TYPE_BLEND_PNT);
		}
    
		if (lpd3dRigidPNTVtxBuf != null)
		{
			STATEMANAGER.SetStreamSource(0, lpd3dRigidPNTVtxBuf, sizeof(SPNTVertex));
			RenderMeshNodeListWithOneTexture(CGrannyMesh.TYPE_RIGID, CGrannyMaterial.TYPE_BLEND_PNT);
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void RenderWithTwoTexture()
	{
		if (IsEmpty())
		{
			return;
		}
    
		STATEMANAGER.SetVertexShader(ms_pntVS);
    
		LPDIRECT3DVERTEXBUFFER8 lpd3dDeformPNTVtxBuf = __GetDeformableD3DVertexBufferPtr();
		LPDIRECT3DVERTEXBUFFER8 lpd3dRigidPNTVtxBuf = m_pModel.GetPNTD3DVertexBuffer();
    
		if (lpd3dDeformPNTVtxBuf != null)
		{
			STATEMANAGER.SetStreamSource(0, lpd3dDeformPNTVtxBuf, sizeof(SPNTVertex));
			RenderMeshNodeListWithTwoTexture(CGrannyMesh.TYPE_DEFORM, CGrannyMaterial.TYPE_DIFFUSE_PNT);
		}
		if (lpd3dRigidPNTVtxBuf != null)
		{
			STATEMANAGER.SetStreamSource(0, lpd3dRigidPNTVtxBuf, sizeof(SPNTVertex));
			RenderMeshNodeListWithTwoTexture(CGrannyMesh.TYPE_RIGID, CGrannyMaterial.TYPE_DIFFUSE_PNT);
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void BlendRenderWithTwoTexture()
	{
		if (IsEmpty())
		{
			return;
		}
    
		LPDIRECT3DVERTEXBUFFER8 lpd3dDeformPNTVtxBuf = __GetDeformableD3DVertexBufferPtr();
		LPDIRECT3DVERTEXBUFFER8 lpd3dRigidPNTVtxBuf = m_pModel.GetPNTD3DVertexBuffer();
    
		 STATEMANAGER.SetVertexShader(ms_pntVS);
    
		if (lpd3dDeformPNTVtxBuf != null)
		{
			STATEMANAGER.SetStreamSource(0, lpd3dDeformPNTVtxBuf, sizeof(SPNTVertex));
			RenderMeshNodeListWithTwoTexture(CGrannyMesh.TYPE_DEFORM, CGrannyMaterial.TYPE_BLEND_PNT);
		}
    
		if (lpd3dRigidPNTVtxBuf != null)
		{
			STATEMANAGER.SetStreamSource(0, lpd3dRigidPNTVtxBuf, sizeof(SPNTVertex));
			RenderMeshNodeListWithTwoTexture(CGrannyMesh.TYPE_RIGID, CGrannyMaterial.TYPE_BLEND_PNT);
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void RenderWithoutTexture()
	{
		if (IsEmpty())
		{
			return;
		}
    
		STATEMANAGER.SetVertexShader(ms_pntVS);
		STATEMANAGER.SetTexture(0, null);
		STATEMANAGER.SetTexture(1, null);
    
		LPDIRECT3DVERTEXBUFFER8 lpd3dDeformPNTVtxBuf = __GetDeformableD3DVertexBufferPtr();
		LPDIRECT3DVERTEXBUFFER8 lpd3dRigidPNTVtxBuf = m_pModel.GetPNTD3DVertexBuffer();
    
		if (lpd3dDeformPNTVtxBuf != null)
		{
			STATEMANAGER.SetStreamSource(0, lpd3dDeformPNTVtxBuf, sizeof(SPNTVertex));
			RenderMeshNodeListWithoutTexture(CGrannyMesh.TYPE_DEFORM, CGrannyMaterial.TYPE_DIFFUSE_PNT);
			RenderMeshNodeListWithoutTexture(CGrannyMesh.TYPE_DEFORM, CGrannyMaterial.TYPE_BLEND_PNT);
		}
    
		if (lpd3dRigidPNTVtxBuf != null)
		{
			STATEMANAGER.SetStreamSource(0, lpd3dRigidPNTVtxBuf, sizeof(SPNTVertex));
			RenderMeshNodeListWithoutTexture(CGrannyMesh.TYPE_RIGID, CGrannyMaterial.TYPE_DIFFUSE_PNT);
			RenderMeshNodeListWithoutTexture(CGrannyMesh.TYPE_RIGID, CGrannyMaterial.TYPE_BLEND_PNT);
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void RenderMeshNodeListWithOneTexture(CGrannyMesh.EType eMeshType, CGrannyMaterial.EType eMtrlType)
	{
		Debug.Assert(m_pModel != null);
    
		LPDIRECT3DINDEXBUFFER8 lpd3dIdxBuf = m_pModel.GetD3DIndexBuffer();
		Debug.Assert(lpd3dIdxBuf != null);
    
		SMeshNode pMeshNode = m_pModel.GetMeshNodeList(eMeshType, eMtrlType);
    
		while (pMeshNode != null)
		{
			CGrannyMesh pMesh = pMeshNode.pMesh;
			int vtxMeshBasePos = pMesh.GetVertexBasePosition();
    
			STATEMANAGER.SetIndices(lpd3dIdxBuf, vtxMeshBasePos);
			STATEMANAGER.SetTransform(D3DTS_WORLD, m_meshMatrices[pMeshNode.iMesh]);
    
			STriGroupNode pTriGroupNode = pMesh.GetTriGroupNodeList(eMtrlType);
			int vtxCount = pMesh.GetVertexCount();
			while (pTriGroupNode != null)
			{
				ms_faceCount += pTriGroupNode.triCount;
    
				CGrannyMaterial rkMtrl = m_kMtrlPal.GetMaterialRef(pTriGroupNode.mtrlIndex);
				rkMtrl.ApplyRenderState();
				STATEMANAGER.DrawIndexedPrimitive(D3DPT_TRIANGLELIST, 0, vtxCount, pTriGroupNode.idxPos, pTriGroupNode.triCount);
				rkMtrl.RestoreRenderState();
    
				pTriGroupNode = pTriGroupNode.pNextTriGroupNode;
			}
    
			pMeshNode = pMeshNode.pNextMeshNode;
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void RenderMeshNodeListWithTwoTexture(CGrannyMesh.EType eMeshType, CGrannyMaterial.EType eMtrlType)
	{
		Debug.Assert(m_pModel != null);
    
		LPDIRECT3DINDEXBUFFER8 lpd3dIdxBuf = m_pModel.GetD3DIndexBuffer();
		Debug.Assert(lpd3dIdxBuf != null);
    
		SMeshNode pMeshNode = m_pModel.GetMeshNodeList(eMeshType, eMtrlType);
    
		while (pMeshNode != null)
		{
			CGrannyMesh pMesh = pMeshNode.pMesh;
			int vtxMeshBasePos = pMesh.GetVertexBasePosition();
    
			STATEMANAGER.SetIndices(lpd3dIdxBuf, vtxMeshBasePos);
			STATEMANAGER.SetTransform(D3DTS_WORLD, m_meshMatrices[pMeshNode.iMesh]);
    
			STriGroupNode pTriGroupNode = pMesh.GetTriGroupNodeList(eMtrlType);
			int vtxCount = pMesh.GetVertexCount();
			while (pTriGroupNode != null)
			{
				ms_faceCount += pTriGroupNode.triCount;
    
				CGrannyMaterial rkMtrl = m_kMtrlPal.GetMaterialRef(pTriGroupNode.mtrlIndex);
				STATEMANAGER.SetTexture(0, rkMtrl.GetD3DTexture(0));
				STATEMANAGER.SetTexture(1, rkMtrl.GetD3DTexture(1));
				STATEMANAGER.DrawIndexedPrimitive(D3DPT_TRIANGLELIST, 0, vtxCount, pTriGroupNode.idxPos, pTriGroupNode.triCount);
				pTriGroupNode = pTriGroupNode.pNextTriGroupNode;
			}
    
			pMeshNode = pMeshNode.pNextMeshNode;
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void RenderMeshNodeListWithoutTexture(CGrannyMesh.EType eMeshType, CGrannyMaterial.EType eMtrlType)
	{
		Debug.Assert(m_pModel != null);
    
		LPDIRECT3DINDEXBUFFER8 lpd3dIdxBuf = m_pModel.GetD3DIndexBuffer();
		Debug.Assert(lpd3dIdxBuf != null);
    
		SMeshNode pMeshNode = m_pModel.GetMeshNodeList(eMeshType, eMtrlType);
    
		while (pMeshNode != null)
		{
			CGrannyMesh pMesh = pMeshNode.pMesh;
			int vtxMeshBasePos = pMesh.GetVertexBasePosition();
    
			STATEMANAGER.SetIndices(lpd3dIdxBuf, vtxMeshBasePos);
			STATEMANAGER.SetTransform(D3DTS_WORLD, m_meshMatrices[pMeshNode.iMesh]);
    
			STriGroupNode pTriGroupNode = pMesh.GetTriGroupNodeList(eMtrlType);
			int vtxCount = pMesh.GetVertexCount();
    
			while (pTriGroupNode != null)
			{
				ms_faceCount += pTriGroupNode.triCount;
				STATEMANAGER.DrawIndexedPrimitive(D3DPT_TRIANGLELIST, 0, vtxCount, pTriGroupNode.idxPos, pTriGroupNode.triCount);
				pTriGroupNode = pTriGroupNode.pNextTriGroupNode;
			}
			pMeshNode = pMeshNode.pNextMeshNode;
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void Update(uint dwAniFPS)
	{
		if (dwAniFPS == 0)
		{
			return;
		}
    
		uint c_dwCurUpdateFrame = (uint)(GetLocalTime() * ANIFPS_MAX);
		uint ANIFPS_STEP = ANIFPS_MAX / dwAniFPS;
		if (c_dwCurUpdateFrame > ANIFPS_STEP && c_dwCurUpdateFrame / ANIFPS_STEP == m_dwOldUpdateFrame / ANIFPS_STEP)
		{
			return;
		}
    
		m_dwOldUpdateFrame = c_dwCurUpdateFrame;
		GrannySetModelClock(m_pgrnModelInstance, GetLocalTime());
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void UpdateLocalTime(float fElapsedTime)
	{
		m_fSecondsElapsed = fElapsedTime;
		m_fLocalTime += fElapsedTime;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void UpdateTransform(D3DXMATRIX pMatrix, float fSecondsElapsed)
	{
		if (!m_pgrnModelInstance)
		{
			TraceError("CGrannyModelIstance::UpdateTransform - m_pgrnModelInstance = NULL");
			return;
		}
		GrannyUpdateModelMatrix(m_pgrnModelInstance, fSecondsElapsed, (float)pMatrix, (float)pMatrix, false);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void Deform(D3DXMATRIX c_pWorldMatrix)
	{
		if (IsEmpty())
		{
			return;
		}
    
		UpdateWorldPose();
		UpdateWorldMatrices(c_pWorldMatrix);
    
		if (m_pModel.CanDeformPNTVertices())
		{
			CGraphicVertexBuffer rkDeformableVertexBuffer = __GetDeformableVertexBufferRef();
			TPNTVertex pntVertices;
			if (rkDeformableVertexBuffer.LockRange(m_pModel.GetDeformVertexCount(), (object) pntVertices))
			{
				DeformPNTVertices(pntVertices);
				rkDeformableVertexBuffer.Unlock();
			}
			else
			{
				TraceError("GRANNY DEFORM DYNAMIC BUFFER LOCK ERROR");
			}
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void UpdateSkeleton(D3DXMATRIX c_pWorldMatrix, float UnnamedParameter)
	{
		UpdateWorldPose();
		UpdateWorldMatrices(c_pWorldMatrix);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void UpdateWorldPose()
	{
		if (m_ppkSkeletonInst)
		{
			if (*m_ppkSkeletonInst != this)
			{
				return;
			}
		}
    
	//# Laniatus Games Studio Inc. |: This static local variable declaration (not allowed in C#) has been moved just prior to the method:
	//	static CGrannyLocalPose s_SharedLocalPose;
    
		granny_skeleton pgrnSkeleton = GrannyGetSourceSkeleton(m_pgrnModelInstance);
		granny_local_pose pgrnLocalPose = UpdateWorldPose_s_SharedLocalPose.Get(pgrnSkeleton.BoneCount);
    
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not have an equivalent to pointers to value types:
	//Original Metin2 CPlus Line: const float * pAttachBoneMatrix = (mc_pParentInstance) ? mc_pParentInstance->GetBoneMatrixPointer(m_iParentBoneIndex) : NULL;
		float pAttachBoneMatrix = (mc_pParentInstance) ? mc_pParentInstance.GetBoneMatrixPointer(m_iParentBoneIndex) : null;
    
		GrannySampleModelAnimationsAccelerated(m_pgrnModelInstance, pgrnSkeleton.BoneCount, pAttachBoneMatrix, pgrnLocalPose, __GetWorldPosePtr());
		GrannyFreeCompletedModelControls(m_pgrnModelInstance);
    
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void UpdateWorldMatrices(D3DXMATRIX c_pWorldMatrix)
	{
		if (!m_meshMatrices)
		{
			return;
		}
    
		Debug.Assert(m_pModel != null);
		Debug.Assert(ms_lpd3dMatStack != null);
    
		int meshCount = m_pModel.GetMeshCount();
    
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not have an equivalent to pointers to value types:
	//Original Metin2 CPlus Line: float * pgrnMatCompositeBuffer[4][4] = GrannyGetWorldPoseComposite4x4Array(__GetWorldPosePtr());
		float  [][] pgrnMatCompositeBuffer = GrannyGetWorldPoseComposite4x4Array(__GetWorldPosePtr());
		D3DXMATRIX[] boneMatrices = (D3DXMATRIX) pgrnMatCompositeBuffer;
    
		for (int LaniatusDefVariables = 0; LaniatusDefVariables < meshCount; ++i)
		{
			D3DXMATRIX rWorldMatrix = m_meshMatrices[LaniatusDefVariables];
    
			CGrannyMesh pMesh = m_pModel.GetMeshPointer(i);
    
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not have an equivalent to pointers to value types:
	//Original Metin2 CPlus Line: int * boneIndices = __GetMeshBoneIndices(i);
			int boneIndices = __GetMeshBoneIndices(i);
    
			if (pMesh.CanDeformPNTVertices())
			{
				rWorldMatrix = c_pWorldMatrix;
			}
			else
			{
				int iBone = boneIndices;
				D3DXMatrixMultiply(rWorldMatrix, boneMatrices[iBone], c_pWorldMatrix);
			}
		}
    
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void DeformPNTVertices(object pvDest)
	{
		Debug.Assert(m_pModel != null);
		Debug.Assert(m_pModel.CanDeformPNTVertices());
    
		m_pModel.DeformPNTVertices(pvDest, (D3DXMATRIX) GrannyGetWorldPoseComposite4x4Array(__GetWorldPosePtr()), m_vct_pgrnMeshBinding);
	}
}