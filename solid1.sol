// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Storage {

    //0xd9145CCE52D386f254917e481eB44e9943F39138
    address private owner;
    mapping(address => uint) public payments;

    constructor() {
        owner = msg.sender;
    }

    function payForItem() public payable {
        payments[msg.sender] = msg.value;
    }

    function withALL() public {
        address payable _to = payable(owner);
        address _thisContr = address(this); 
        _to.transfer(_thisContr.balance);
    }
}
