// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract AccessControl {
    address public admin;
    mapping(address => Role) public userRoles;

    enum Role { NoAccess, Read, Write, ReadWrite }

    event RoleAssigned(address indexed user, Role role);
    event AccessRevoked(address indexed user);

    constructor() {
        admin = msg.sender;
    }

    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can perform this action");
        _;
    }

    function assignRole(address user, Role role) public onlyAdmin {
        userRoles[user] = role;
        emit RoleAssigned(user, role);
    }

    function revokeRole(address user) public onlyAdmin {
        userRoles[user] = Role.NoAccess;
        emit AccessRevoked(user);
    }

    function canRead(address user) public view returns (bool) {
        Role role = userRoles[user];
        return role == Role.Read || role == Role.ReadWrite;
    }

    function canWrite(address user) public view returns (bool) {
        Role role = userRoles[user];
        return role == Role.Write || role == Role.ReadWrite;
    }
}
