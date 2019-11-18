# Copyright (c) 2018, Red Hat, Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

# ====================================+
# COPIED FROM ember-csi, then modified
# ====================================+

from __future__ import absolute_import

from google.protobuf import wrappers_pb2 as wrappers

from . import csi_pb2


class EnumWrapper(object):
    def __init__(self, enum):
        self._enum = enum

    def __getattr__(self, name):
        try:
            return getattr(self._enum, name)
        except AttributeError:
            return self._enum.Value(name)


Bool = wrappers.BoolValue

InfoResp = csi_pb2.GetPluginInfoResponse
NodeInfoResp = csi_pb2.NodeGetInfoResponse

Capability = csi_pb2.PluginCapability
Service = Capability.Service
ServiceType = EnumWrapper(Service.Type)
CtrlCapability = csi_pb2.ControllerServiceCapability
CtrlCapabilityType = EnumWrapper(CtrlCapability.RPC.Type)
CtrlCapabilityResp = csi_pb2.ControllerGetCapabilitiesResponse

NodeCapability = csi_pb2.NodeServiceCapability
NodeCapabilityType = EnumWrapper(NodeCapability.RPC.Type)
NodeCapabilityResp = csi_pb2.NodeGetCapabilitiesResponse

ListResp = csi_pb2.ListVolumesResponse
ValidateResp = csi_pb2.ValidateVolumeCapabilitiesResponse

CtrlPublishResp = csi_pb2.ControllerPublishVolumeResponse
CtrlUnpublishResp = csi_pb2.ControllerUnpublishVolumeResponse

CapabilitiesResp = csi_pb2.GetPluginCapabilitiesResponse
AccessModeType = EnumWrapper(csi_pb2.VolumeCapability.AccessMode.Mode)

StageResp = csi_pb2.NodeStageVolumeResponse
UnstageResp = csi_pb2.NodeUnstageVolumeResponse
NodePublishResp = csi_pb2.NodePublishVolumeResponse
NodeUnpublishResp = csi_pb2.NodeUnpublishVolumeResponse
ProbeRespOK = csi_pb2.ProbeResponse(ready=Bool(value=True))
CapacityResp = csi_pb2.GetCapacityResponse
CreateResp = csi_pb2.CreateVolumeResponse
DeleteResp = csi_pb2.DeleteVolumeResponse
Volume = csi_pb2.Volume

VolumeContentSource = csi_pb2.VolumeContentSource
VolumeSource = csi_pb2.VolumeContentSource.VolumeSource
SnapshotSource = csi_pb2.VolumeContentSource.SnapshotSource

Snapshot = csi_pb2.Snapshot
CreateSnapResp = csi_pb2.CreateSnapshotResponse
DeleteSnapResp = csi_pb2.DeleteSnapshotResponse
ListSnapResp = csi_pb2.ListSnapshotsResponse
SnapEntry = ListSnapResp.Entry

VolumeStatsResp = csi_pb2.NodeGetVolumeStatsResponse
VolumeUsage = csi_pb2.VolumeUsage
UsageUnit = EnumWrapper(VolumeUsage.Unit)

Topology = csi_pb2.Topology
