/*
  Warnings:

  - Added the required column `password` to the `User` table without a default value. This is not possible if the table is not empty.

*/
-- DropForeignKey
ALTER TABLE `loans` DROP FOREIGN KEY `loans_ibfk_2`;

-- DropForeignKey
ALTER TABLE `loans` DROP FOREIGN KEY `loans_ibfk_1`;

-- AlterTable
ALTER TABLE `user` ADD COLUMN     `password` VARCHAR(191) NOT NULL;

-- AddForeignKey
ALTER TABLE `Loans` ADD FOREIGN KEY (`userId`) REFERENCES `User`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `Loans` ADD FOREIGN KEY (`bookId`) REFERENCES `Book`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;
