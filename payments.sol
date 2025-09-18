// SPDX-License-Identifier: UNLICENSED

pragma solidity ^0.8.28;


contract payments {

    address owner;

    event Paid(address indexed _from, uint _amount, uint _timestamp);


    constructor() {
        owner = msg.sender;
    }

    receive() external payable {
    }

    function pay() external payable {
        emit Paid(msg.sender, msg.value, block.timestamp);
    }

    modifier onlyOwner(address _to) {
        require(msg.sender == owner, "you are not an owner");
        require(_to != address(0), "incorrect addr");
        _;
        // require(...);
    }

    function withdraw(address payable _to) external onlyOwner(_to) {
        // Panic
        // assert(msg.sender == owner);

        // require(msg.sender == owner, "you are not owner");
        // if(msg.sender != owner) {
        //     revert("you are not GGG");
        // }

        _to.transfer(address(this).balance);
    }


    // Struct
    // struct Payment {
    //     uint ammount;
    //     uint timestap;
    //     address from;
    //     string message;
        
    // }

    // struct Balance {
    //     uint totalPayments;
    //     mapping(uint => Payment) payments;
    // }

    // mapping(address => Balance) public balances;

    // function getPayment(address _addr, uint _index) public view returns(Payment memory) {
    //     return balances[_addr].payments[_index];
    // }

    // function pay(string memory message) public payable returns(uint) {
    //     uint paymentNum = balances[msg.sender].totalPayments;
    //     balances[msg.sender].totalPayments++;

    //     Payment memory newPayment = Payment(
    //         msg.value,
    //         block.timestamp,
    //         msg.sender,
    //         message
    //     );

    //     balances[msg.sender].payments[paymentNum] = newPayment;

    //     return msg.value;
    // }
}
