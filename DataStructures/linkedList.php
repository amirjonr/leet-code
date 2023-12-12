<?php

class LinkedList {
    public function __construct(
        public int $data,
        public ?LinkedList $next = null
    ) {}
}

$list = new LinkedList(1);
$list->next = new LinkedList(2);
$list->next->next = new LinkedList(3);

printLinkedList($list);

function printLinkedList(LinkedList $node) {
    while ($node) {
        echo $node->data . " -> ";
        $node = $node->next;
    }
    print('None');
}