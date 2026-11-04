from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSkillsFilesListOutput, DashboardInstanceSkillsFilesListOutput, mapDashboardInstanceSkillsFilesGetOutput, DashboardInstanceSkillsFilesGetOutput, mapDashboardInstanceSkillsFilesGetQuery, DashboardInstanceSkillsFilesGetQuery, mapDashboardInstanceSkillsFilesPutOutput, DashboardInstanceSkillsFilesPutOutput, mapDashboardInstanceSkillsFilesPutBody, DashboardInstanceSkillsFilesPutBody, mapDashboardInstanceSkillsFilesDeleteOutput, DashboardInstanceSkillsFilesDeleteOutput, mapDashboardInstanceSkillsFilesDeleteQuery, DashboardInstanceSkillsFilesDeleteQuery, mapDashboardInstanceSkillsFilesMoveOutput, DashboardInstanceSkillsFilesMoveOutput, mapDashboardInstanceSkillsFilesMoveBody, DashboardInstanceSkillsFilesMoveBody, mapDashboardInstanceSkillsFilesBatchOutput, DashboardInstanceSkillsFilesBatchOutput, mapDashboardInstanceSkillsFilesBatchBody, DashboardInstanceSkillsFilesBatchBody

class MetorialDashboardInstanceSkillsFilesEndpoint(BaseMetorialEndpoint):
    """Read and edit the files of a skill by path."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, skill_id: str) -> DashboardInstanceSkillsFilesListOutput:
        """
    List skill files
    Lists every file of a skill with its path, size and etag. Directories are implied by file paths.

    :param instance_id: str
    :param skill_id: str
    :return: DashboardInstanceSkillsFilesListOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'skills', skill_id, 'files']
        )
        return self._get(request).transform(mapDashboardInstanceSkillsFilesListOutput.from_dict)

    def get(self, instance_id: str, skill_id: str, *, path: str) -> DashboardInstanceSkillsFilesGetOutput:
        """
    Get skill file
    Retrieves a single skill file by path. Documents include their text content, other files include a download URL.

    :param instance_id: str
    :param skill_id: str
    :param path: str
    :return: DashboardInstanceSkillsFilesGetOutput
    """
        # Build query parameters from keyword arguments
        query_dict = {}
        query_dict["path"] = path

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'skills', skill_id, 'files', 'content'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceSkillsFilesGetOutput.from_dict)

    def put(self, instance_id: str, skill_id: str, *, path: str, content: Optional[str] = None, file_id: Optional[str] = None, if_match: Optional[str] = None) -> DashboardInstanceSkillsFilesPutOutput:
        """
    Write skill file
    Creates or replaces the file at a path. Parent directories are created automatically.

    :param instance_id: str
    :param skill_id: str
    :param path: str
    :param content: Optional[str] (optional)
    :param file_id: Optional[str] (optional)
    :param if_match: Optional[str] (optional)
    :return: DashboardInstanceSkillsFilesPutOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["path"] = path
        if content is not None:
            body_dict["content"] = content
        if file_id is not None:
            body_dict["file_id"] = file_id
        if if_match is not None:
            body_dict["if_match"] = if_match

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'skills', skill_id, 'files'],
            body=body_dict
        )
        return self._put(request).transform(mapDashboardInstanceSkillsFilesPutOutput.from_dict)

    def delete(self, instance_id: str, skill_id: str, *, path: str, if_match: Optional[str] = None) -> DashboardInstanceSkillsFilesDeleteOutput:
        """
    Delete skill file
    Deletes the file at a path. Directories that were created automatically and become empty are removed. The root SKILL.md cannot be deleted.

    :param instance_id: str
    :param skill_id: str
    :param path: str
    :param if_match: Optional[str] (optional)
    :return: DashboardInstanceSkillsFilesDeleteOutput
    """
        # Build query parameters from keyword arguments
        query_dict = {}
        query_dict["path"] = path
        if if_match is not None:
            query_dict["if_match"] = if_match

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'skills', skill_id, 'files'],
            query=query_dict
        )
        return self._delete(request).transform(mapDashboardInstanceSkillsFilesDeleteOutput.from_dict)

    def move(self, instance_id: str, skill_id: str, *, path: str, to_path: str, if_match: Optional[str] = None) -> DashboardInstanceSkillsFilesMoveOutput:
        """
    Move skill file
    Moves or renames a file. The root SKILL.md cannot be moved.

    :param instance_id: str
    :param skill_id: str
    :param path: str
    :param to_path: str
    :param if_match: Optional[str] (optional)
    :return: DashboardInstanceSkillsFilesMoveOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["path"] = path
        body_dict["to_path"] = to_path
        if if_match is not None:
            body_dict["if_match"] = if_match

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'skills', skill_id, 'files', 'move'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceSkillsFilesMoveOutput.from_dict)

    def batch(self, instance_id: str, skill_id: str, *, changes: List[Union[Dict[str, Any], Dict[str, Any], Dict[str, Any]]]) -> DashboardInstanceSkillsFilesBatchOutput:
        """
    Apply skill file changes
    Applies up to 100 put, delete and move changes one after another, in order. Every change is validated before any is applied, but changes are not applied atomically: if a change fails while being applied, the changes before it stay applied. Every change can carry its own if_match precondition.

    :param instance_id: str
    :param skill_id: str
    :param changes: List[Union[Dict[str, Any], Dict[str, Any], Dict[str, Any]]]
    :return: DashboardInstanceSkillsFilesBatchOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["changes"] = changes

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'skills', skill_id, 'files', 'batch'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceSkillsFilesBatchOutput.from_dict)