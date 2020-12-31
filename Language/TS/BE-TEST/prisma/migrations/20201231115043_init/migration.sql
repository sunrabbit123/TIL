-- CreateTable
CREATE TABLE `User` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `email` VARCHAR(191),
    `name` VARCHAR(191) NOT NULL,
    `age` INT NOT NULL,
UNIQUE INDEX `User.email_unique`(`email`),

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- CreateTable
CREATE TABLE `Book` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `title` VARCHAR(191) NOT NULL,
    `description` VARCHAR(191) NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- CreateTable
CREATE TABLE `Loans` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `userId` INT NOT NULL,
    `bookId` INT NOT NULL,
UNIQUE INDEX `Loans.userId_unique`(`userId`),
UNIQUE INDEX `Loans.bookId_unique`(`bookId`),

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- AddForeignKey
ALTER TABLE `Loans` ADD FOREIGN KEY (`userId`) REFERENCES `User`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `Loans` ADD FOREIGN KEY (`bookId`) REFERENCES `Book`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;
