package com.axis.bank.controllers;

import com.axis.bank.entities.Customer;
import com.axis.bank.entities.Employee;
import com.axis.bank.repositories.EmployeeRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import javax.persistence.EntityNotFoundException;

@CrossOrigin(origins = "http://localhost:3001")
@RestController
@RequestMapping("/api/employee")
public class EmployeeController {
    @Autowired
    private EmployeeRepository employeeRepository;
    @GetMapping("/{employeeId}")
    public ResponseEntity<Employee> getEmployeeByEmployeeId(@PathVariable String employeeId) {
        Employee employee = employeeRepository.findByEmployeeId(employeeId)
                .orElseThrow(()-> new RuntimeException("Error getting Employee"));
        return ResponseEntity.ok(employee);
    }
    @PutMapping
    public ResponseEntity<Employee> updateCustomer(@RequestBody Employee employee) {
        Employee employee1 = employeeRepository.findByEmployeeId(employee.getEmployeeId())
                .orElseThrow(()-> new RuntimeException("Error getting Employee"));
        employee.setId(employee1.getId());
        return ResponseEntity.ok(employeeRepository.save(employee));
    }
    @ExceptionHandler(EntityNotFoundException.class)
    public String entityNotFound(){return "Customer Does Not Exits.."; }
}
